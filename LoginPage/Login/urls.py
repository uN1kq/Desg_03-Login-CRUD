from django.urls import path 
from . import views

urlpatterns = [ 
	path('', views.homepage_name, name='homepage_name'),
	path('/second', views.secondpage_name, name='secondpage_name'),
]