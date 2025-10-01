from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('django.contrib.auth.urls')), 
   path('', include('blog.urls')),
   path('blog/', include('blog.urls')),
   path('accounts/', include('django.contrib.auth.urls')),
]
    

