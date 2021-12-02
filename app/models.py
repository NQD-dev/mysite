from django.db import models

# Create your models here.
class Catalog_left(models.Model):
    catalogID = models.CharField(db_column='catalog_id',max_length=20, unique=True)
    catalogName = models.CharField(db_column='catalog_name', max_length=100)

class Brand(models.Model):
    brandID = models.CharField(db_column='brand_id',max_length=20, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='uploads/', null = True)

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    productID = models.CharField(db_column='product_id',max_length=20, unique=True)
    title = models.CharField(max_length=200, blank=True, null=False)
    title2 = models.CharField(max_length=500, blank=True, null=True)
    summary = models.CharField(max_length=500, blank=True, null=False)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    price = models.IntegerField(default=0)
    price_old = models.IntegerField(default=0)
    description = models.TextField()
    status = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    internal_storage = models.CharField(max_length=50, blank=True, null=True, default=None)
    color = models.CharField(max_length=100, blank=True, null=True)
    style = models.CharField(max_length=100, blank=True, null=True)
    season = models.CharField(max_length=100, blank=True, null=True)
    usage = models.CharField(max_length=100, blank=True, null=True)
    sport = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(Catalog_left, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    TYPE_PRODUCT = (
        ('N', 'New'),
        ('F', 'Featured'),
    )
    type_products = models.CharField(max_length=1, choices=TYPE_PRODUCT, null=False, default='F')

    def __str__(self):
        return f'{self.title}, {self.description}'

class Product_image(models.Model):
    image = models.ImageField(upload_to='uploads/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.title} image'

class UpcomingProducts(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    price = models.IntegerField(default=0)
    color = models.CharField(max_length=100, blank=True, null=True)
    style = models.CharField(max_length=100, blank=True, null=True)
    season = models.CharField(max_length=100, blank=True, null=True)
    usage = models.CharField(max_length=100, blank=True, null=True)
    sport = models.CharField(max_length=100, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

class MainProduct(models.Model):
    title = models.CharField(max_length=200, null= True)
    title2 = models.CharField(max_length=200, null= True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)