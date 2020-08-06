from django.urls import path
from . import views
urlpatterns = [
    
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),


    path('', views.index, name='user_index'),
    path('update/', views.user_update, name='user_update'),
    #path('password/', views.user_password, name='user_password'),
    path('purchases/', views.user_orders, name='user_orders'),
    path('favorites', views.user_favorites, name='user_favorites'),
    #path('orders_product/', views.user_order_product, name='user_order_product'),
    #path('orderdetail/<int:id>', views.user_orderdetail, name='user_orderdetail'),
    #path('order_product_detail/<int:id>/<int:oid>', views.user_order_product_detail, name='user_order_product_detail'),
    #path('comments/', views.user_comments, name='user_comments'),
    #path('deletecomment/<int:id>', views.user_deletecomment, name='user_deletecomment'),


]