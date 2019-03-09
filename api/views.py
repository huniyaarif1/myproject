from django.shortcuts import render
from api.models import Ads
from api.models import Product
from rest_framework import generics
from rest_framework import filters  
from api.serializers import AdSerializer
from api.serializers import ProductSerializer
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

class ProductDetail(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get(self, reques):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        queryset = Product.objects.all()
