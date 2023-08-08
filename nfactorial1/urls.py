from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name='blog-home'),
    path('<int:first>/add/<int:second>/' , views.sum , name = 'nfactorial1.sum' ),
    path('transform/<str:text>/' , views.up , name = 'nfactorial1.upper' ),
    path('check/<str:word>/' , views.pal , name = 'nfactorial1.pol' ),
    path('calc/<int:first>/<str:operation>/<int:second>/' , views.calc , name = 'nfactorial1.calc' )
]