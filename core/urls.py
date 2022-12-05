from django.contrib import admin
from django.urls import path, include
from core.views import index, create_listing
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.create_listing, name='create_listing'),
]