from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #url(r'^$', 'customforms.views.index'),
    url(r'^show/(?P<name>.+)/$', 'customforms.views.show_form'),
    url(r'^get/(?P<name>.+)/$', 'customforms.views.get_form'),
    url(r'^list$', 'customforms.views.list_forms'),
)
