from django.core.management.base import BaseCommand, CommandError
from .models import *

OC_URL = "http://opencoesione.gov.it/api/territori.json?page=1"

class Command(BaseCommand):
	args = '<poll_id poll_id ...>'
	help = 'Closes the specified poll for voting'



	def handle(self, *args, **options):
		next_url = OC_URL
		while next_url is not None:
			jj = requests.get(next_url).json()
			next_url = jj.get('next')
			for result in jj.get('results'): 
				if result.get('slug') is not None:
					l = Location()
					l.name = slug
					l.save()