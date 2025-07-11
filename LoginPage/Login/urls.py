from django.urls import path 
from . import views

urlpatterns = [ 
	path('', views.page_name, name='page_name'),
]