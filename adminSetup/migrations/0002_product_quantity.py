# Generated by Django 4.0.2 on 2022-11-20 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminSetup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
