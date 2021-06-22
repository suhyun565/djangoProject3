from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from speedracer.models import *

class Inventory(models.Model):
    product = models.ForeignKey('speedracer.Product', on_delete=models.CASCADE,null=True)
    order = models.ForeignKey('speedracer.Order', on_delete=models.CASCADE,blank=True,null=True)
    quantity = models.PositiveIntegerField(null=True)
    current_amount = models.FloatField(blank=True,default=0,null=True)
    created = models.DateTimeField(blank=True,null=True)

    def save(self, *args, **kwargs):
        if self.order.status == 'Entering':
            self.current_amount = self.order.count + self.quantity
        elif self.order.status == 'Releasing':
            self.current_amount = self.quantity - self.order.count
        else:
            self.current_amount = self.quantity
        return super().save(*args, **kwargs)
