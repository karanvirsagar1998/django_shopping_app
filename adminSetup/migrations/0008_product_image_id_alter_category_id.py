# Generated by Django 4.0.2 on 2022-11-23 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminSetup', '0007_productimages_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]