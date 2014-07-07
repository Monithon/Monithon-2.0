from django.core.management.base import BaseCommand, CommandError
from projects.models import *

from time import sleep
import requests 

class Command(BaseCommand):
    def handle(self, *args, **options):

        OC_URL = "http://opencoesione.gov.it/api/nature.json?page=1"

        """

        {
            "count": 6, 
            "next": null, 
            "previous": null, 
            "results": [
                {
                    "filters": {
                        "progetti": "http://opencoesione.gov.it/api/progetti?natura=conferimenti-capitale", 
                        "soggetti": "http://opencoesione.gov.it/api/soggetti?natura=conferimenti-capitale"
                    }, 
                    "codice": "08", 
                    "descrizione": "ACQUISTO DI PARTECIPAZIONI AZIONARIE E CONFERIMENTI DI CAPITALE", 
                    "short_label": " Conferimenti capitale", 
                    "slug": "conferimenti-capitale"
                }
            ]
        }

        """

        next_url = OC_URL
        while next_url is not None or next_url != "" or next_url != u"None":
            try:
                jj = requests.get(next_url).json()
                if "next" in jj:
                    next_url = jj.get('next')
                    print ">>>", next_url
                    for result in jj.get('results'): 
                        print result
                        try:
                            l = Tags()
                            l.slug = result.get('slug')
                            l.name = result.get('short_label')
                            l.description = result.get('descrizione')
                            l.tagtype = "natura"
                            l.save()
                        except:
                            pass
                else:
                    sleep(5)
            except:
                pass


        OC_URL = "http://opencoesione.gov.it/api/temi.json?page=1"

        """

        {
            "count": 13, 
            "next": null, 
            "previous": null, 
            "results": [
                {
                    "filters": {
                        "progetti": "http://opencoesione.gov.it/api/progetti?tema=agenda-digitale", 
                        "soggetti": "http://opencoesione.gov.it/api/soggetti?tema=agenda-digitale"
                    }, 
                    "codice": "7", 
                    "descrizione": "Agenda digitale", 
                    "short_label": "Agenda digitale", 
                    "slug": "agenda-digitale"
                }
            ]
        }

        """

        next_url = OC_URL
        while next_url is not None or next_url != "" or next_url != "None":
            jj = requests.get(next_url).json()
            if "next" in jj:
                next_url = jj.get('next')
                print ">>>", next_url
                for result in jj.get('results'): 
                    print result
                    l = Tags()
                    l.slug = result.get('slug')
                    l.name = result.get('short_label')
                    l.description = result.get('descrizione')
                    l.tagtype = "tema"
                    l.save()
            else:
                sleep(5)
