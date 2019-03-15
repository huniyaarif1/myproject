# api/serializers.py

from api.models import Product
from api.models import FavouriteInfo
from api.models import UserData
from api.models import Category
from api.models import Item
from rest_framework import serializers
from django.core.files.base import ContentFile

class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class FavouriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FavouriteInfo
        depth=1
        fields = ('productid','user_id',)

class ProductSerializer(serializers.ModelSerializer):
    fav_products = FavouriteSerializer(many=True)
    image_one=Base64ImageField(max_length=None, use_url=True)
    image_two=Base64ImageField(max_length=None, use_url=True)
    image_three=Base64ImageField(max_length=None, use_url=True)
    image_four=Base64ImageField(max_length=None, use_url=True)
    image_five=Base64ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = Product
        fields = ('id','product_id','user_ID','title', 'description','category', 'subcategories', 'city',
                  'address', 'price', 'negotiable',
                  'new', 'used','contact', 'image_one','image_two','image_three', 'image_four','image_five','addto_favourite','fav_products')

    def create(self, validated_data):
        fav_data = validated_data.pop('fav_products')
        favID = Product.objects.create(**validated_data)
        for f_data in fav_data:
            FavouriteInfo.objects.create(favID=favID, **f_data)
        return favID


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
        fields = ('image','category','subcategories')

    def create(self, validated_data):
        category_data = validated_data.pop('subcategories')
        cID = Item.objects.create(**validated_data)
        for cat_data in category_data:
            Category.objects.create(cID=cID, **cat_data)
        return cID
        
        


