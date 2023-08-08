from django.urls import path
from . import views
urlpatterns = [
	path('nfactorial/', views.home, name='blog-home'),
    path('nfactorial/<int:first>/add/<int:second>/' , views.sum , name = 'blog.sum' )
]