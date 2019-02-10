"""
Url patterns for the index.
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='auth-login'),
    path('logout/', views.logout, name='auth-logout'),
    path('robots.txt', views.robots, name='robots'),
]
