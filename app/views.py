from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *

@api_view(['GET','POST'])
def getAllCatalogLeft(request, fomart = None):
    catalogLefts = [Catalog_leftSerializer(catalogLeft).data 
        for catalogLeft in Catalog_left.objects.all()]
    return Response(catalogLefts)

@api_view(['GET','POST'])
def getAllUpcomingProducts(request):
    upcomingProducts = [UpcomingProductsSerializer(upcomingProduct).data 
        for upcomingProduct in UpcomingProducts.objects.all()]
    return Response(upcomingProducts)

@api_view(['GET','POST'])
def getAllMainProducts(request):
    mainProducts = [MainProductsSerializer(mainProduct).data 
        for mainProduct in MainProduct.objects.all()]
    return Response(mainProducts)

@api_view(['GET','POST'])
def getAllProducts(request):
    products = [ProductsSerializer(product).data 
        for product in Product.objects.all()]
    return Response(products)

@api_view(['GET','POST'])
def getAllNewProducts(request):
    newProducts = [ProductsSerializer(product).data 
        for product in Product.objects.filter(type_products='N')]
    return Response(newProducts)

@api_view(['GET','POST'])
def getAllFeaturedProducts(request):
    featureProducts = [ProductsSerializer(product).data 
        for product in Product.objects.filter(type_products='F')]
    return Response(featureProducts)

@api_view(['GET','POST'])
def getAllBrands(request):
    brands = [BrandSerializer(brand).data 
        for brand in Brand.objects.all()]
    return Response(brands)

@api_view(['GET'])
def getProductDetail(request, pk):
    product = Product.objects.filter(pk=pk).first()
    if product:
        data = ProductsSerializer(product).data
        return Response(data)
    else:
        return Response({'error': 'Not found'})

@api_view(['GET','POST'])
def getCatalogProducts(request, pk):
    catalogProducts = [ProductsSerializer(product).data 
        for product in Product.objects.filter(category=pk)]
    return Response(catalogProducts)