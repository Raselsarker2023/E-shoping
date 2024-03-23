from django.db import models
from django.contrib.auth.models import User
from django.utils.functional import cached_property
from products.models import ProductModel
from .constants import STATUS_CHOICES


class Order(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['-created_at',]


    def __str__(self):
        return str(self.name) if self.name is not None else 'Unnamed Product'
    
    
    
    # def __str__(self):
    #     return f"{self.email} - {self.created_at.strftime('%b. %-d, %Y, %-I:%M %p')}"

    @cached_property
    def total_cost(self):
        """
        Total cost of all the items in an order
        """
        return round(sum([order_item.cost for order_item in self.order_items.all()]), 2)



class OrderList(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, related_name='items', on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return '%s' % self.id
    
