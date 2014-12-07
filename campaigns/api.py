from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'campaigns.views.api_campaings'),
    url(r'^(?P<campaign_id>\d+)$', 'campaigns.views.api_campaings'),
)
