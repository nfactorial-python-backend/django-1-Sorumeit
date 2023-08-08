from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name='blog-home'),
    path('<int:first>/add/<int:second>/' , views.sum , name = 'blog.sum' )
]