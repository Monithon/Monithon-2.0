from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'campaigns.views.campaigns'),
    url(r'^(?P<campaign_id>\d+)$', 'campaigns.views.campaigns'),
    url(r'^(?P<campaign_id>\d+)/add$', 'campaigns.views.add_project'),
    url(r'^(?P<campaign_id>\d+)/endorse$', 'campaigns.views.endorse'),
    url(r'^(?P<campaign_id>\d+)/unendorse$', 'campaigns.views.unendorse'),
)
