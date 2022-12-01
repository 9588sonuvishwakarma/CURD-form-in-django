from django.urls import path,include
from .import views

urlpatterns = [
    path('open ', views.open, name="open"),
    path('start', views.start, name="start"),

  ]