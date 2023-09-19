from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.index , name="index") , #if not thing comes after 127.0.0.1 go to the urls of our app (competition)
]