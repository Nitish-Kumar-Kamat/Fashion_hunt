from django.contrib import admin

from .models import Result
class resadmin(admin.ModelAdmin):
    list_display=('sno','cname','type','team','status','prize')
admin.site.register(Result,resadmin)
