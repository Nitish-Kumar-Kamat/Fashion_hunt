from django.contrib import admin

from .models import Feedback
class feedadmin(admin.ModelAdmin):
    list_display=('id','name','contact','email','suggestion')
admin.site.register(Feedback,feedadmin)
