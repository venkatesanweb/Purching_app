# Generated by Django 5.1.7 on 2025-03-21 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop_Fusion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_image',
            new_name='image',
        ),
    ]
