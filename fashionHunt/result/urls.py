from django.urls import path
from .import views

urlpatterns=[
   path('',views.result, name="result"),
   path('resTask/',views.resTask, name="resTask"),
   path('resShow/',views.resShow, name="resShow"),
]