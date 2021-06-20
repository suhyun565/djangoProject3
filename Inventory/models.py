from django.db import models
from speedracer.models import Product, Order
from django.utils import timezone
from django.shortcuts import reverse

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,blank=True,null=True)
    quantity = models.PositiveIntegerField()
    current_amount = models.FloatField(blank=True,default=0)
    created = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if self.order.status == 'Entering':
            self.current_amount = self.order.count + self.quantity
        elif self.order.status == 'Releasing':
            self.current_amount = self.quantity - self.order.count
        else:
            self.current_amount = self.quantity
        return super().save(*args, **kwargs)
