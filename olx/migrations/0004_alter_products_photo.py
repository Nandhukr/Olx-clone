# Generated by Django 4.1.2 on 2023-02-15 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0003_alter_products_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile.images'),
        ),
    ]
