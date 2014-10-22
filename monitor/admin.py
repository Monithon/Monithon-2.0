from django.contrib import admin

# Register your models here.


from monitor.models import *

admin.site.register(MonitoringTeam)
admin.site.register(Monitor)