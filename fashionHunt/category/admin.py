from django.contrib import admin

from .models import Category
class catadmin(admin.ModelAdmin):
    list_display=('cid','cname','image')
admin.site.register(Category,catadmin)
