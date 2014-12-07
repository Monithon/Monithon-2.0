from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Campaign)
admin.site.register(CampaignProject)
admin.site.register(CampaignForm)
admin.site.register(CampaignReport)