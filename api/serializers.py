# api/serializers.py

from api.models import Ads
from api.models import Product
from api.models import Favourite
from api.models import User
from rest_framework import serializers
        
class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ('id','user_id','category', 'subcategories', 'city',
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
        fields = ('id','user_id','product_id')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','user_id','username','email','usertype','loggedin')


