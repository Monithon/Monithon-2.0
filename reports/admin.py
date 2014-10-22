from django.contrib import admin

# Register your models here.

from reports.models import * 


admin.site.register(Report)
admin.site.register(ReportForm)
admin.site.register(ReportFormField)
admin.site.register(ReportLink)