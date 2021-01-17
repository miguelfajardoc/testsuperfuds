from django.db import models
from datetime import date
from django import utils


class Warehouse(models.Model):
    name = models.CharField(max_length=150, default='')
    headquartersNumber = models.IntegerField()
    created_at = models.DateTimeField(default=utils.timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Warehouse_description(models.Model):
    phone = models.IntegerField()
    city = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(default=utils.timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    warehouse_id = models.ForeignKey(Warehouse, related_name='description', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return(self.city)