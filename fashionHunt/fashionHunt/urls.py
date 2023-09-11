from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('signup/',include('signup.urls')),
    path('audition/',include('audition.urls')),
    path('category/',include('category.urls')),
    path('about/',include('aboutus.urls')),
    path('feedback/',include('feedback.urls')),
    path('result/',include('result.urls')),
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
