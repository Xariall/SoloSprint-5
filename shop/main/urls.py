from django.urls import path
from . import views

# 
urlpatterns = [
    path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    
    path('login/', views.customer_login, name="login"),
    path('register/', views.customer_register, name="register"),

    path('products/<int:product_id>', views.product_detail, name='product_detail'),
]
