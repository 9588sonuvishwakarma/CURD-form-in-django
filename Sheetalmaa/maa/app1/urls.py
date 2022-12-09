from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.home,name="home"),
path('product/',views.product,name="product"),
path('customer/<int:pk_test>/', views.customer,name="customer"),
 path('create_order/',views.createOrder,name="create_order"),
    path('update_order/<str:pk>/',views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/',views.deleteOrder, name="delete_order"),


]