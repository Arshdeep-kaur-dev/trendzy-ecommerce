from django.urls import path
from . import views

urlpatterns = [
    path('',                        views.home,             name='home'),
    path('product/<int:pk>/',       views.product_detail,   name='product_detail'),
    path('register/',               views.register_view,    name='register'),
    path('login/',                  views.login_view,       name='login'),
    path('logout/',                 views.logout_view,      name='logout'),
    path('cart/',                   views.cart_view,        name='cart'),
    path('cart/add/<int:pk>/',      views.add_to_cart,      name='add_to_cart'),
    path('cart/remove/<int:pk>/',   views.remove_from_cart, name='remove_from_cart'),
    path('checkout/',               views.place_order,      name='checkout'),
    path('orders/',                 views.my_orders,        name='my_orders'),
]