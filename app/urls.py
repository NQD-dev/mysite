from django.urls import path
from .views import *

urlpatterns = [
    path('catalog_left_all/', getAllCatalogLeft),
    path('upcoming_products/', getAllUpcomingProducts),
    path('main_products/',getAllMainProducts),
    path('new_products/',getAllNewProducts),
    path('all_products/',getAllProducts),
    path('feature_products/',getAllFeaturedProducts),
    path('all_brands/',getAllBrands),
    path('product_detail/<pk>', getProductDetail),
    path('catalog_product/<pk>', getCatalogProducts),
]