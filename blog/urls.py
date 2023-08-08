from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name='blog-home'),
    path('<int:first>/add/<int:second>/' , views.sum , name = 'blog.sum' ),
    path('transform/<str:text>/' , views.up , name = 'blog.upper' ),
    path('check/<str:word>/' , views.pol , name = 'blog.pol' )
]