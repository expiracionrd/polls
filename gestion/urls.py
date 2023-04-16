from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('polls', views.polls),
    path('voted', views.voted),
    path('live', views.results),
    path('api/token', views.getRoutes),
    path('api/token/refresh', views.getRoutes),
    path('accounts/', include('django.contrib.auth.urls')),

]