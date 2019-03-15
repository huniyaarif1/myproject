from django.db import models

# Create your models here.

class UserData(models.Model):
    user_ID=models.CharField(max_length=200, unique=True)
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200, blank=True)
    usertype=models.CharField(max_length=20)
    loggedin=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    product_id = models.CharField(unique=True,max_length= 50, null=False)
    user_ID=models.CharField(max_length=200)
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
    image_one = models.ImageField(upload_to = 'myproject/static', default = '')
    image_two = models.ImageField(blank=True,null=True,upload_to = 'myproject/static', default = '')
    image_three = models.ImageField(blank=True,null=True,upload_to = 'myproject/static', default = '')
    image_four = models.ImageField(blank=True,null=True,upload_to = 'myproject/static', default = '')
    image_five = models.ImageField(blank=True, null=True,upload_to = 'myproject/static', default = '')


class FavouriteInfo(models.Model):
    favID = models.ForeignKey(Product, related_name='fav_products', on_delete = models.CASCADE)
    user_id=models.CharField(max_length=200, blank=True)
    productid=models.CharField(max_length=200)
            
class Item(models.Model):
    category = models.CharField(max_length=50)
    image=models.URLField(max_length=250)

class Category(models.Model):
    cID = models.ForeignKey(Item, related_name='subcategories', on_delete = models.CASCADE)
    subcategory = models.CharField(max_length=30)


