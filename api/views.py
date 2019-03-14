from django.shortcuts import render
from api.models import Ads
from api.models import Product
from api.models import FavouriteInfo
from api.models import UserData
from api.models import Category
from api.models import Item
from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response
from api.serializers import AdSerializer
from api.serializers import ItemSerializer
from api.serializers import CategorySerializer
from api.serializers import ProductSerializer
from api.serializers import FavouriteSerializer
from api.serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.views import APIView
import base64
from django.core.files.base import ContentFile

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
            response_data={}
            response_data["success"] = "True"
            response_data["message"] = "Settings created successfully."
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        aid = request.GET.get('aid')
        ad = Ads.objects.get(id=aid)
        ad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request):
        aid = request.GET.get('aid')
        ad = Ads.objects.get(id=aid)
        serializer = AdSerializer(ad, data=request.data)
        # validate and update
        if serializer.is_valid():
            serializer.save()
            response_data={}
            response_data["success"] = "True"
            response_data["message"] = "Settings updated successfully."
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    
    def get_queryset(self):
        queryset = Item.objects.all()
        #serializer = CategorySerializer(queryset, many=True)
        #data = serializer.data
        return queryset
    
    def post(self,request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data={}
            response_data["success"] = "True"
            response_data["message"] = "Settings updated successfully."
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

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
            response_data=serializer.data
            response_data["success"] = "True"
            response_data["message"] = "Settings created successfully."
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FavouriteDetail(generics.ListAPIView):

    queryset = FavouriteInfo.objects.all()
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
            response_data={}
            response_data["success"] = "True"
            response_data["message"] = "Settings created successfully."
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        userid = request.GET.get('userid')
        productid = request.GET.get('productid')
        fav = FavouriteInfo.objects.get(productid=productid,user_ID=userid)
        fav.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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

    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data={}
            response_data["success"] = "True"
            response_data["message"] = "Settings created successfully."
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProductSearch(generics.ListAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)
