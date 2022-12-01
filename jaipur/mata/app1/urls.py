from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.basic,name='basic'),


    path('mainhome/',views.mainhome,name='mainhome'),
    path('about/',views.about,name='about'),





]