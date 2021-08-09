from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ytd_down, name='index'),
    path('download/', views.yt_down, name='download'),
]