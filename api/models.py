from django.db import models

# Create your models here.

class UserData(models.Model):
    user_ID=models.CharField(max_length=200, unique=True)
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200, blank=True)
    usertype=models.CharField(max_length=20)
    loggedin=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Ads(models.Model):
    user_ID=models.CharField(max_length=200)
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
    contact = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to = 'static', default = 'static/education_category.png')#models.ImageField(max_length=None, allow_empty_file=False, use_url=True)

class Product(models.Model):
    pID = models.CharField(primary_key=True, max_length= 50, null=False)
    title=models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    subcategories = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    negotiable=models.BooleanField(default=False)
    new=models.BooleanField(default=False)
    used=models.BooleanField(default=False)
    addto_favourite=models.BooleanField(default=False)
    contact = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to = 'static', default = 'static/education_category.png')#models.ImageField(max_length=None, allow_empty_file=False, use_url=True)

class FavouriteInfo(models.Model):
    pID = models.ForeignKey(Product, to_field='pID', related_name='fav_products', on_delete = models.CASCADE)
    user_ID=models.CharField(max_length=200)
    product_id=models.CharField(max_length=200)
        
class Item(models.Model):
    cID = models.CharField(primary_key=True, max_length= 50, null=False)
    category = models.CharField(max_length=50)
    image=models.URLField(max_length=250)

class Category(models.Model):
    cID = models.ForeignKey(Item, related_name='subcategories', to_field='cID', on_delete = models.CASCADE)
    subcategory = models.CharField(max_length=30)


