from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('cart/', views.cart, name="cart"),
    path('checkoutdetails/', views.checkoutdetails, name="checkoutdetails"),
    path('checkoutshipping/', views.checkoutshipping, name="checkoutshipping"),
    path('checkoutpayments/', views.checkoutpayments, name="checkoutpayments"),
    path('checkoutreview/', views.checkoutreview, name="checkoutreview"),
    path('checkoutcomplete/', views.checkoutcomplete, name="checkoutcomplete"),
    path('ordertracking/', views.ordertracking, name="ordertracking"),
    path('single/', views.single, name="single"),
    

]