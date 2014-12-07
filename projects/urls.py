from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'projects.views.list_projects'),
    url(r'^search$', 'projects.views.search'),
    url(r'^(?P<cup>\d+)$', 'projects.views.get_project'),
    url(r'^(?P<project_id>\d+)/upload$', 'uploads.views.upload'),
    url(r'^(?P<project_id>\d+)/files/(?P<upload_id>\d+)$', 'uploads.views.download'),

    
    #url(r'^show/(?P<name>\w+)/$', 'customforms.views.show_form'),
    #url(r'^get/(?P<name>\w+)/$', 'customforms.views.get_form'),
)
