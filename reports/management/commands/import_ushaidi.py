from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import Point
from customforms.models import * 
from reports.models import *

import xml.etree.ElementTree as ET

from datetime import datetime

U_FILE = "ushaidi.xml"

class Command(BaseCommand):
	def handle(self, *args, **options):

		Report.objects.all().delete()

		tree = ET.parse(U_FILE)
		root = tree.getroot()
		#for el in tree.findall("//custom_forms/form"):
		#	f = Form()
		#	f.name = el.find("title").text
		#	print "> FORM"
		#	print el.find("title").text
		#	f.save()
		#	for fi in el.findall("field"):
		#		print ">> FIELD"
		#		ffo = FormFieldOption()
		#		ffo.label = fi.find("name").text
		#		print fi.find("name").text
		#		ffo.form = f
		#		ffo.form_field = FormField.objects.get(name="textarea") if fi.attrib.get("type") == "2" else FormField.objects.get(name="radio")
		#		ffo.hint = ""
		#		if fi.find("default") is not None:
		#			ffo.options = fi.find("default").text.replace(",", "\n")
		#		ffo.save()
		#	ffo = FormFieldOption()
		#	ffo.label = "Descrizione"
		#	ffo.form = f
		#	ffo.form_field=FormField.objects.get(name="textarea")
		#	ffo.hint = ""
		#	ffo.save()

		for el in tree.findall("//reports/report"):
			r = Report()

			r.validated = el.attrib.get("verified") == "1"
			r.finalized = el.attrib.get("approved") == "1"
			f = el.find("custom_fields")
			for fi in f.findall("field"):
				if fi.attrib.get("name") == "URL OpenCoesione":
					print "OC>> ", fi.text.replace("progetti", "api/progetti")[:-1]+".json"
					try:
						r.project = Monitorable.objects.get(oc_url=fi.text.replace("progetti", "api/progetti")[:-1]+".json")
					except:
						print "REPORT",el.attrib.get("id"), "not found"
				if fi.attrib.get("name") == "Nome/i e Cognome/i":
					r.author_text = fi.text
			r.datetime = datetime.strptime(el.find("dateadd").text, "%Y-%m-%d %H:%M:%S")
			r.title = el.find("title").text

			lon = float(el.find("location").find("longitude").text)
			lat = float(el.find("location").find("latitude").text)

			r.position = Point(lon, lat)

			r.save()
			rf = ReportForm()
			rf.report = r
			rf.form = CustomForm.objects.get(name=el.attrib.get("form_name"))
			rf.save()
			f = el.find("custom_fields")
			for fi in f.findall("field"):
				rff = ReportFormField()
				rff.report_form = rf
				rff.field = FormFieldOption.objects.get(form__name=el.attrib.get("form_name"), label=fi.attrib.get("name"))
				rff.value = fi.text
				rff.save()

			rff.report_Form = rf
			rff.field = FormFieldOption.objects.get(form__name=el.attrib.get("form_name"), label="Descrizione")
			rff.value = el.find("description").text
			rff.save()
			for m in el.findall("media/item"):
				rl = ReportLink()
				rl.report = r
				rl.link = m.text
				rl.save()

