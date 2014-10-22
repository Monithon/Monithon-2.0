from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'monitor.views.list_teams'),
    url(r'^(?P<id>\d+)$', 'monitor.views.list_teams'),
    url(r'^(?P<id>\d+)/join$', 'monitor.views.list_teams', {"op":"join"}),
    url(r'^(?P<id>\d+)/leave$', 'monitor.views.list_teams', {"op":"leave"}),
    #url(r'^show/(?P<name>\w+)/$', 'customforms.views.show_form'),
    #url(r'^get/(?P<name>\w+)/$', 'customforms.views.get_form'),
)
