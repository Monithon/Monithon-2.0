from django.core.management.base import BaseCommand, CommandError
from projects.models import *



from time import sleep
import requests 

OC_URL = "http://opencoesione.gov.it/api/soggetti.json?page=1"

"""

{
    "count": 73898, 
    "next": "http://opencoesione.gov.it/api/soggetti?page=2", 
    "previous": null, 
    "page_size": 25, 
    "current_page": 1, 
    "last_page": 2956, 
    "facet_counts": {
        "ruolo": [
            "attuatore (73826)", 
            "programmatore (3079)"
        ], 
        "tema": [
            "occupazione (24056)", 
            "istruzione (20540)", 
            "ricerca-e-innovazione (15732)", 
            "competitivita-imprese (8978)", 
            "agenda-digitale (6091)", 
            "inclusione-sociale (4338)", 
            "energia (4170)", 
            "cultura-e-turismo (2763)", 
            "ambiente (1827)", 
            "infanzia-e-anziani (1565)", 
            "citta-e-aree-rurali (1018)", 
            "rafforzamento-pa (533)", 
            "trasporti (489)"
        ]
    }, 
    "results": [
        {
            "url": "http://opencoesione.gov.it/api/soggetti/ministero-delle-infrastrutture-e-dei-trasporti-97532760580", 
            "denominazione": "ministero delle infrastrutture e dei trasporti", 
            "tema": [
                "ambiente", 
                "competitivita-imprese", 
                "cultura-e-turismo", 
                "inclusione-sociale", 
                "istruzione", 
                "rafforzamento-pa", 
                "trasporti"
            ], 
            "ruolo": [
                "programmatore", 
                "attuatore"
            ], 
            "costo": 8878334000.0, 
            "n_progetti": 4213
        }]
}
"""

class Command(BaseCommand):
	def handle(self, *args, **options):
		next_url = OC_URL
		while next_url is not None or next_url != "" or next_url != "None":
			jj = requests.get(next_url).json()
			if "next" in jj:
				next_url = jj.get('next')
				print ">>>", next_url
				for result in jj.get('results'): 
					print result
					l = Subject()
					l.name = result.get('denominazione') if result.get('denominazione') is not None else "-"
					l.url = result.get('url')
					l.save()
			else:
				sleep(5)
