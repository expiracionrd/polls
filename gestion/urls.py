from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('index',views.index),
    path('polls', views.polls),
    path ('voted', views.voted)
]