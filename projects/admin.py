from django.contrib import admin

# Register your models here.

from projects.models import *

# Register your models here.

admin.site.register(Location)
admin.site.register(Geo)
admin.site.register(Subject)
admin.site.register(Tag)
admin.site.register(Monitorable)
admin.site.register(MonitorableCategory)