"""
Url patterns for the index.
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('robots.txt', views.robots, name='robots'),
]
