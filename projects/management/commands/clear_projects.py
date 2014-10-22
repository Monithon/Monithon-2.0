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
		Monitorable.objects.all().delete()