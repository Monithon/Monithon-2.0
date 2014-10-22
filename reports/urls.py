from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'new$', 'reports.views.new_report'),
	url(r'push$', 'reports.views.push_report'),
    url(r'(?P<id>\d+)$', 'reports.views.show_report'),
    url(r'geojson$', 'reports.views.reports_json'),
    url(r'$', 'reports.views.list_reports'),



)
