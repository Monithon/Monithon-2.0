from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'monithon.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^projects/', include('projects.urls')),
    #url(r'^monitorers/', include('monitor.urls')),
    url(r'^reports/', include('reports.urls')),
    url(r'^forms/', include('customforms.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^accounts/login/$', "monithon.views.logins"),
    url(r'^accounts/logout$', "monithon.views.logout_view"),
    url(r'^accounts/profile/$', "monithon.views.profile", name="profile"),
    url(r'^accounts/profile/(?P<username>.*)$', "monithon.views.profile", name="profile_user"),
    url(r'^accounts/', include('social.apps.django_app.urls', namespace='social'))
)
