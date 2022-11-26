from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=1000, null=True)

    class Meta:
        db_table = "categories"


class SubCategory(models.Model):
    name = models.CharField(max_length=100, null=True)
    category_id = models.IntegerField(null=True)
    description = models.TextField(max_length=1000, null=True)

    class Meta:
        db_table = "subcategories"


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField(null=True)
    sub_category_id = models.IntegerField(null=True)  # type of product
    initial_price = models.FloatField(null=True)  # striked one
    discount = models.FloatField(null=True)
    final_price = models.FloatField(null=True)
    color = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
    date_created = models.DateField(null=True, auto_now_add=True)
    sales = models.IntegerField(null=True)
    image_id = models.IntegerField(null=True)

    class Meta:
        db_table = "products"


class ProductImages(models.Model):
    product_id = models.IntegerField(null=True)
    image1 = models.ImageField(blank=True, default=None, upload_to='products')
    image2 = models.ImageField(blank=True, default=None, upload_to='products')
    image3 = models.ImageField(blank=True, default=None, upload_to='products')
    image4 = models.ImageField(blank=True, default=None, upload_to='products')
    image5 = models.ImageField(blank=True, default=None, upload_to='products')

    class Meta:
        db_table = 'product_images'