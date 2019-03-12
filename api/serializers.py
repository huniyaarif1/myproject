# api/serializers.py

from api.models import Ads
from api.models import Product
from api.models import Favourite
from api.models import UserData
from api.models import CategoryInfo
from rest_framework import serializers
        
class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ('id','user_ID','category', 'subcategories', 'city',
                  'address', 'title', 'description', 'price', 'negotiable',
                  'new', 'used', 'contact', 'image')

        
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id','category', 'subcategories', 'city',
                  'address', 'title', 'description', 'price', 'negotiable',
                  'new', 'used', 'contact', 'image')
    
class FavouriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favourite
        fields = ('id','user_ID','product_id')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ('id','user_ID','username','email','usertype','loggedin')


class CategorySerializer(serializers.ModelSerializer):

    subcategories = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = CategoryInfo
        fields = ('category','subcategories')


