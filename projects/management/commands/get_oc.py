import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from django.core.management.base import BaseCommand, CommandError
from projects.models import *

from bs4 import BeautifulSoup 

import os
import time
import requests 
import json
import zipfile
import csv


base_url ="http://opencoesione.gov.it"
init = base_url + "/opendata/"

files = {
	"Progetti":"prj",
	"Soggetti":"sub",
	"Localizzazioni":"loc",
	#"Pagamenti":"pay.csv",
}

class Command(BaseCommand):
	def handle(self, *args, **options):
		r = requests.get(init)
		r = BeautifulSoup(r.text)

		for kind in files.keys():
			for row in  r.find_all("table")[0].find_all("tr"):
				tr = row.find_all("td")
				if tr[0].string.strip() == kind:
					nurl = base_url + tr[1].find_all("a")[0]["href"]
					c = requests.get(nurl)
					if not os.path.exists(files[kind]+".csv"):
						with open(files[kind]+".zip", "wb") as out:
							out.write(c.content)
							print "file dled", kind
						with open(files[kind]+".csv", "wb") as out:
							print "extracting"
							with zipfile.ZipFile(files[kind]+".zip") as zz:
								for filename in zz.namelist():
									out.write(zz.open(filename).read())

						os.remove(files[kind]+".zip")


		with open("sub.csv", "rb") as sub:
			subr = csv.DictReader(sub, delimiter=";")
			for row in subr:
				print row
				break

		with open("loc.csv", "rb") as loc:
			locr = csv.DictReader(loc, delimiter=";")
			for row in locr:
				print row
				break

		with open("prj.csv", "rb") as prj:
			prjr = csv.DictReader(prj, delimiter=";")
			for row in prjr:
				print "\n".join(row.keys())
				break

