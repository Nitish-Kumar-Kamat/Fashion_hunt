from django.contrib import admin

from .models import Audition_Reg
class audiservice(admin.ModelAdmin):
	list_display=('id','name','email','place','date','image')
admin.site.register(Audition_Reg,audiservice)

