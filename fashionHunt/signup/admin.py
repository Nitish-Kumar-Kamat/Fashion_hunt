from django.contrib import admin

from .models import Registration
class regservice(admin.ModelAdmin):
	list_display=('id','name','email','mobile','address','image')
admin.site.register(Registration,regservice)

