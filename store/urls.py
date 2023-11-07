from django.urls import path

from . import views
from .views import  login_page, register_page, cart

from django.urls import path
from .views import product_detail



urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('login', login_page),
    path('register', register_page,),
path('register.html', register_page, name='register'),

	path('request/', views.send_request, name='request'),
	path('verify/', views.verify, name='verify'),





    path('product/<int:pk>/', product_detail, name='product_detail'),






]
