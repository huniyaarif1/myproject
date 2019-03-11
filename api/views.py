from django.shortcuts import render
from api.models import Ads
from api.models import Product
from api.models import Favourite
from rest_framework import generics
from rest_framework import filters  
from api.serializers import AdSerializer
from api.serializers import ProductSerializer
from api.serializers import FavouriteSerializer
from rest_framework.permissions import AllowAny

# Create your views here.

class AdDetail(generics.ListAPIView):

    queryset = Ads.objects.all()
    serializer_class = AdSerializer
    
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """        
        userid = self.request.query_params.get('userid', None)
        if userid:
            queryset = self.queryset.filter(user_id=userid)
        return queryset
    
class FavouriteDetail(generics.ListAPIView):

    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """        
        userid = self.request.query_params.get('userid', None)
        if userid:
            queryset = self.queryset.filter(user_id=userid)
        return queryset

class ProductFilterDetail(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """        
        cat = self.request.query_params.get('cat', None)
        scat = self.request.query_params.get('scat', None)
        queryset = Product.objects.all()
        if cat:
            if cat:
                queryset = self.queryset.filter(category=cat)
            if scat:
                queryset = queryset.filter(subcategories=scat)       
        return queryset

class ProductSearch(generics.ListAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)
