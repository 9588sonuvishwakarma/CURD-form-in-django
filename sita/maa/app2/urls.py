from django.urls import path,include
from .import views

urlpatterns = [
    path('end', views.end, name="end"),
    path('start', views.start, name="start"),
    path('own', views.own, name="own"),

  ]