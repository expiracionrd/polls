from api.urls import path
from api.views import *

from . import views

urlpatterns = [
    path('api/token', views.getRoutes),
    path('api/token/refresh', views.getRoutes)
]
