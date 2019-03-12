from django.shortcuts import render
from api.models import Ads
from api.models import Product
from api.models import Favourite
from api.models import UserData
from api.models import CategoryInfo
from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response
from api.serializers import AdSerializer
from api.serializers import CategorySerializer
from api.serializers import ProductSerializer
from api.serializers import FavouriteSerializer
from api.serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status 

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
            queryset = self.queryset.filter(user_ID=userid)
        return queryset
    
    def post(self,request):
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(generics.ListAPIView):
    serializer_class = CategorySerializer
    
    def get(self, request):
        cat = CategoryInfo.objects.all()
        serializer = CategorySerializer(cat, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

class UserDetail(generics.ListAPIView):

    queryset = UserData.objects.all()
    serializer_class = UserSerializer
    
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """        
        userid = self.request.query_params.get('userid', None)
        if userid:
            queryset = self.queryset.filter(user_ID=userid)
        return queryset

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
            queryset = self.queryset.filter(user_ID=userid)
        return queryset
    
    def post(self,request):
        serializer = FavouriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
