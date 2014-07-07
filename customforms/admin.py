from django.contrib import admin

from customforms.models import *

# Register your models here.

admin.site.register(Form)
admin.site.register(FormField)
admin.site.register(FormFieldOption)