# Generated by Django 4.0.2 on 2022-11-20 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminSetup', '0005_alter_category_table_alter_product_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='categories',
        ),
        migrations.AlterModelTable(
            name='product',
            table='products',
        ),
        migrations.AlterModelTable(
            name='subcategory',
            table='subcategories',
        ),
    ]
