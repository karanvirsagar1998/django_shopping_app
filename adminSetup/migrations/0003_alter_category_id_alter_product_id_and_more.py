# Generated by Django 4.1.3 on 2022-11-20 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminSetup', '0002_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
