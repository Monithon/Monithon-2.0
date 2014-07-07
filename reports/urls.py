from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'reports.views.list_reports'),
    url(r'^new$', 'reports.views.new_report'),
	url(r'^push$', 'reports.views.push_report'),


)
