# api/resources.py

from tastypie.resources import ModelResource
from api.models import Ads
from api.models import User
from api.models import Category
from api.models import Product
from api.models import Favourite
from tastypie.authorization import Authorization

class AdsResource(ModelResource):
    class Meta:
        queryset = Ads.objects.all()
        resource_name = 'ads'
        authorization = Authorization()

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        authorization = Authorization()


class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'
        authorization = Authorization()

class FavouriteResource(ModelResource):
    class Meta:
        queryset = Favourite.objects.all()
        resource_name = 'favourite'
        authorization = Authorization()


