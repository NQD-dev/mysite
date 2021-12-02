# Generated by Django 3.2.5 on 2021-11-26 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandID', models.CharField(db_column='brand_id', max_length=20, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productID', models.CharField(db_column='product_id', max_length=20, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('price', models.IntegerField(default=0)),
                ('price_old', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('internal_storage', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('color', models.CharField(max_length=100)),
                ('style', models.CharField(max_length=100)),
                ('season', models.CharField(max_length=100)),
                ('usage', models.CharField(max_length=100)),
                ('sport', models.CharField(max_length=100)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.catalog_left')),
            ],
        ),
        migrations.CreateModel(
            name='UpcomingProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('price', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=100)),
                ('style', models.CharField(max_length=100)),
                ('season', models.CharField(max_length=100)),
                ('usage', models.CharField(max_length=100)),
                ('sport', models.CharField(max_length=100)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Product_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]