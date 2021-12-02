# Generated by Django 3.2.5 on 2021-11-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog_left',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalogID', models.CharField(db_column='catalog_id', max_length=20, unique=True)),
                ('catalogName', models.CharField(db_column='catalog_name', max_length=100)),
            ],
        ),
    ]