from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('' , views.index , name="index") , 
    path('vote/<int:id>' , views.vote , name="vote") ,
    path('result' , views.result , name="result")
]