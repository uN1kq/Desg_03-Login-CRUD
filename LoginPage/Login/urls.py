from django.urls import path 
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [ 
    path('', views.LoginView, name='login'),
    path('register/', views.RegisterView, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]