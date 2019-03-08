from django.db import models

# Create your models here.

class Ads(models.Model):
    userId=models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    subcategories = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    negotiable=models.BooleanField(default=False)
    new=models.BooleanField(default=False)
    used=models.BooleanField(default=False)
    contact = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=200)#models.ImageField(max_length=None, allow_empty_file=False, use_url=True)

"""
class Category(models.Model):
    category = models.CharField(max_length=200)
    subcategories = models.CharField(max_length=1000)

class Product(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

class Favourite(models.Model):
    productID = models.CharField(max_length=1000)

"""
