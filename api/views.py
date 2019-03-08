from django.shortcuts import render
from api.models import Ads
from rest_framework import generics
from api.serializers import AdSerializer

# Create your views here.

class AdDetail(generics.RetrieveAPIView):
    serializer_class = AdSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Ads.objects.filter(userId=user)
