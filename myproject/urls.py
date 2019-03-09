"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import AdDetail
from api.resources import AdsResource
from api.resources import UserResource
from api.resources import CategoryResource
from api.resources import ProductResource
from api.resources import FavouriteResource
from django.conf.urls import url, include

ads_resource = AdsResource()
category_resource = CategoryResource()
user_resource = UserResource()
product_resource = ProductResource()
favourite_resource = FavouriteResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/ads/get', AdDetail.as_view()),
    url(r'^api/', include(ads_resource.urls)),
    url(r'^api/', include(user_resource.urls)),
    url(r'^api/', include(category_resource.urls)),
    url(r'^api/', include(product_resource.urls)),
    url(r'^api/', include(favourite_resource.urls)),
]
