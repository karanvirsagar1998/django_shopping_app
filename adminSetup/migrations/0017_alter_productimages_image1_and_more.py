# Generated by Django 4.0.2 on 2022-11-23 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminSetup', '0016_delete_test_alter_category_id_alter_product_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='image1',
            field=models.ImageField(blank=True, default=None, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='image2',
            field=models.ImageField(blank=True, default=None, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='image3',
            field=models.ImageField(blank=True, default=None, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='image4',
            field=models.ImageField(blank=True, default=None, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='image5',
            field=models.ImageField(blank=True, default=None, upload_to='products'),
        ),
    ]