# api/serializers.py

from api.models import Ads
from api.models import Product
from api.models import Favourite
from api.models import UserData
from api.models import Category
from api.models import Item
from rest_framework import serializers
        
class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ('ad_ID','user_ID','category', 'subcategories', 'city',
                  'address', 'title', 'description', 'price', 'negotiable',
                  'new', 'used', 'contact', 'image')

        
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('product_id','category', 'subcategories', 'city',
                  'address', 'title', 'description', 'price', 'negotiable',
                  'new', 'used', 'contact', 'image')
    
class FavouriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favourite
        fields = ('id','user_ID','product_id','category', 'subcategories', 'city',
                  'address', 'title', 'description', 'price', 'negotiable',
                  'new', 'used', 'contact', 'image')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ('id','user_ID','username','email','usertype','loggedin')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('subcategory',)
        
class ItemSerializer(serializers.ModelSerializer):
    subcategories = CategorySerializer(many=True)

    class Meta:
        model = Item
        fields = ('cID', 'image','category','subcategories')

    def create(self, validated_data):
        category_data = validated_data.pop('subcategories')
        cID = Item.objects.create(**validated_data)
        for cat_data in category_data:
            Category.objects.create(cID=cID, **cat_data)
        return cID
        
        


