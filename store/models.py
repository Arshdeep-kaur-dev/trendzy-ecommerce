from django.db import models
from django.contrib.auth.models import User

# username->shopping
# password->12345


# Create your models here.

class Category(models.Model):
    name  = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
 
    def __str__(self):
        return self.name
 
    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name        = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    old_price   = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock       = models.PositiveIntegerField(default=0)
    category    = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    image       = models.ImageField(upload_to='products/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.name
    
     
    def discount_percent(self):
        if self.old_price:
            return int((1 - self.price / self.old_price) * 100)
        return 0

class Cart(models.Model):
    user       = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"{self.user.username}'s Cart"
 
    def total(self):
        return sum(item.subtotal() for item in self.cartitem_set.all())

class CartItem(models.Model):
    cart     = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
 
    def subtotal(self):
        return self.product.price * self.quantity

class Order(models.Model):
    STATUS = [
        ('pending',   'Pending'),
        ('confirmed', 'Confirmed'),
        ('shipped',   'Shipped'),
        ('delivered', 'Delivered'),
    ]
    user             = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price      = models.DecimalField(max_digits=10, decimal_places=2)
    status           = models.CharField(max_length=20, choices=STATUS, default='pending')
    shipping_address = models.TextField()
    created_at       = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'Order #{self.id} — {self.user.username}'


class OrderItem(models.Model):
    order    = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product  = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price    = models.DecimalField(max_digits=10, decimal_places=2)


