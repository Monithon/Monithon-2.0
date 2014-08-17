from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'projects.views.list_projects'),
    url(r'^(?P<cup>.+)$', 'projects.views.get_project'),
    #url(r'^show/(?P<name>\w+)/$', 'customforms.views.show_form'),
    #url(r'^get/(?P<name>\w+)/$', 'customforms.views.get_form'),
)
