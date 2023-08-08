from django.contrib import admin
from django.urls import path, include
 
urlpatterns = [
	path('admin/', admin.site.urls),
	path('nfactorial/', include('nfactorial1.urls')),
]