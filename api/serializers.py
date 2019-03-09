# api/serializers.py

from api.models import Ads
from api.models import Product
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
        fields = ('category', 'subcategories', 'city',
                  'address', 'title', 'description', 'price', 'negotiable',
                  'new', 'used', 'contact', 'image')


