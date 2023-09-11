from django.urls import path
from .import views

urlpatterns=[
   path('',views.category,name="categorypage"),
   path('categoryTask/',views.categoryTask, name="categoryTask"),
   path('catshow/',views.catshow, name="catshow"),
]