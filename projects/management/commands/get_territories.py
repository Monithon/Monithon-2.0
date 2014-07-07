from django.core.management.base import BaseCommand, CommandError
from projects.models import *



import requests 

OC_URL = "http://opencoesione.gov.it/api/territori.json?page=1"

"""

{
count: 8238,
next: "http://opencoesione.gov.it/api/territori.json?page=2",
previous: null,
results: [
{
denominazione: "ABRUZZO",
denominazione_ted: null,
territorio: "R",
slug: "abruzzo-regione",
cod_reg: 13,
cod_prov: 0,
cod_com: 0
}]

"""

class Command(BaseCommand):
	def handle(self, *args, **options):
		next_url = OC_URL
		while next_url is not None or next_url != "" or next_url != "None":
			jj = requests.get(next_url).json()
			if "next" in jj:
				next_url = jj.get('next')
				for result in jj.get('results'): 
					print ">>>", next_url
					if result.get('slug') is not None:
						print result
						l = Location()
						l.name = result.get('slug')
						l.slug = result.get('slug')
						l.save()
			else:
				from time import sleep
				time.sleep(5)
