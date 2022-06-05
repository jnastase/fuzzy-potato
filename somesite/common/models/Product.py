from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    added_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)