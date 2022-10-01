from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginForm, name='login'),
    path('logout/', views.logoutForm, name='logout'),
    path('registration/', views.registerForm, name='registration'),
]