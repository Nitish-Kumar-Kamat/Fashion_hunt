from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.reg,name="register"),
    path('regTask/',views.regTask, name="regTask"),
    path('login/',views.login, name="loginpage"),
    path('loginTask/',views.loginTask,name="loginTask"),
    path('audition/',views.audition, name="audition"),


]
