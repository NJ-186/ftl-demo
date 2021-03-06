from django.contrib import admin

from .models import USER, ActivityPeriod

# Register your models here.

admin.site.register(USER)
admin.site.register(ActivityPeriod)