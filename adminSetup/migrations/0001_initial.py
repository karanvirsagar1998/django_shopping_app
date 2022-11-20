# Generated by Django 4.0.2 on 2022-11-20 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(max_length=1000, null=True)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('sub_category_id', models.IntegerField(null=True)),
                ('initial_price', models.FloatField(null=True)),
                ('discount', models.FloatField(null=True)),
                ('final_price', models.FloatField(null=True)),
                ('color', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('sales', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('category_id', models.IntegerField(null=True)),
                ('description', models.TextField(max_length=1000, null=True)),
            ],
            options={
                'db_table': 'subcategories',
            },
        ),
    ]