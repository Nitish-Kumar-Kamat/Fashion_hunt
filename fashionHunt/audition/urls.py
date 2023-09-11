from django.urls import path
from .import views

urlpatterns=[
   path('',views.audi,name="audireg"),
   path('audiTask/',views.audiTask, name="audiTask"),
]
