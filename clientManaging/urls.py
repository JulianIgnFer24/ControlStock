from django.urls import path
from . import views

urlpatterns = [
    path('', views.addClient, name='clients')
]

