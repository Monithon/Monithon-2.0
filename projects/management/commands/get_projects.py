from django.core.management.base import BaseCommand, CommandError
from projects.models import *

import time
import requests 

OC_URL = "http://opencoesione.gov.it/api/progetti.json?page=1"


"""

{
count: 754328,
next: "http://opencoesione.gov.it/api/progetti.json?page=2",
previous: null,
page_size: 25,
current_page: 1,
last_page: 30174,
facet_counts: {},
results: [
{
slug: "1ca1c272007it161po009",
url: "http://opencoesione.gov.it/api/progetti/1ca1c272007it161po009.json",
codice_locale: "1CA1C272007IT161PO009",
cup: "B66E83000000009",
titolo_progetto: "GRANDE PROGETTO. COMPLETAMENTO LINEA 1 DELLA METROPOLITANA DI NAPOLI",
fin_totale_pubblico: 1376000000,
pagamento: 482329952,
perc_pagamento: 35.053047,
soggetti: [
"http://opencoesione.gov.it/api/soggetti/comune-di-napoli-80014890638.json",
"http://opencoesione.gov.it/api/soggetti/regione-campania-80011990639.json"
],
territori: [
"napoli-comune"
],
tema: [
"trasporti"
],
natura: [
"lavori-pubblici"
],
data_inizio_effettiva: "2000-01-01",
data_fine_effettiva: null
}]

"""

class Command(BaseCommand):
	def handle(self, *args, **options):
		next_url = OC_URL
		while next_url is not None:

			mc = MonitorableCategory.objects.get(name="OpenCoesione")

			jj = requests.get(next_url).json()
			if "next" in jj:
				next_url = jj.get('next')
				for result in jj.get('results'): 
					if result.get('slug') is not None:
						print result
						l = Monitorable()
						l.category = mc
						l.cup = result.get("cup")
						l.oc_slug = result.get("slug")
						l.oc_url = result.get("url")
						l.total_amount = result.get("fin_totale_pubblico")
						l.paid_amount = result.get("pagamento")
						l.paid_percent = result.get("perc_pagamento")
						l.description = result.get("titolo_progetto")
						l.date_from = result.get("data_inizio_effettiva")
						l.date_to = result.get("data_fine_effettiva")
						l.save()
						if result.get("soggetti") is not None:
							for s in result.get("soggetti"):
								for sub in Subject.objects.filter(url=s):
									l.subjects.add(sub)
									
						if result.get("territori") is not None:
							for t in result.get("territori"):
								for ter in Location.objects.filter(slug=t):
									l.locations.add(ter)

						if result.get("tema") is not None:
							for t in result.get("tema"):
								for tag in Tag.objects.filter(slug=t):
									l.tags.add(tag)

			
			else:
				time.sleep(5)