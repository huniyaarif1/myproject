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
from api.views import FavouriteDetail
from api.views import UserDetail
from api.views import ProductFilterDetail
from api.views import ProductSearch
from api.views import CategoryDetail
from django.conf.urls import url, include


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/ads', AdDetail.as_view()),
    url(r'^api/favourite', FavouriteDetail.as_view()),
    url(r'^api/product/filter', ProductFilterDetail.as_view()),
    url(r'^api/product/find', ProductSearch.as_view()),
    url(r'^api/user', UserDetail.as_view()),
    url(r'^api/category', CategoryDetail.as_view()),
]
