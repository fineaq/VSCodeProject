from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main),
    path('main/', views.main, name='main'),
    path('login/',views.login_view, name='login'),
    path('signup/',views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]