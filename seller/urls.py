from django.urls import path
from . import views
urlpatterns = [
    path('', views.sellerindex, name="sellerindex"),
    path('sellerdashboard/', views.sellerdashboard, name="sellerdashboard"),



]