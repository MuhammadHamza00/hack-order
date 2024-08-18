from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    DELIVERY_CHOICES = [
        ('pickup', 'Pickup'),
        ('delivery', 'Delivery'),
    ]

    PAYMENT_CHOICES = [
        ('card', 'Card'),
        ('cash', 'Cash'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    selected_items = models.TextField()
    delivery_option = models.CharField(max_length=10, choices=DELIVERY_CHOICES)
    delivery_address = models.CharField(max_length=255, null=True, blank=True)
    pickup_date = models.DateField(null=True, blank=True)
    pickup_time = models.TimeField(null=True, blank=True)
    payment_option = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    card_number = models.CharField(max_length=16, null=True, blank=True)
    expiry_date = models.CharField(max_length=5, null=True, blank=True)
    cvv = models.CharField(max_length=3, null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order by {self.name} - {self.selected_items}'
