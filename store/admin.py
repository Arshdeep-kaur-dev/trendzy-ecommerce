from django.contrib import admin
from .models import Category, Product, Cart, CartItem, Order, OrderItem
 
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display  = ['name', 'price', 'stock', 'category', 'is_featured']
    list_editable = ['price', 'stock', 'is_featured']
    list_filter   = ['category']
    search_fields = ['name']
 
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display  = ['id', 'user', 'total_price', 'status', 'created_at']
    list_editable = ['status']
 
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(OrderItem)
