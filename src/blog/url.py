from django.urls import path                # -2c
from . import views

urlpatterns = [
    path('', views.home, name= 'index_url'),
]

