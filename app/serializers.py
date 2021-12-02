from django.db import models
from rest_framework import fields, serializers
from .models import *

class Catalog_leftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog_left
        fields = ('catalogID', 'catalogName')

class UpcomingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcomingProducts
        fields = ('title','image','price','color','style','season','usage','sport','brand')

class MainProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainProduct
        fields = ('title', 'title2', 'image')

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('productID','title','title2','summary','image','price','price_old','description','status','date_posted',
        'internal_storage','color','style','season','usage','sport','brand','type_products')

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('brandID', 'name', 'description', 'image')