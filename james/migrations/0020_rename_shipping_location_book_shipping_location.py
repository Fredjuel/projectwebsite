# Generated by Django 4.0.7 on 2022-12-01 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('james', '0019_rename_shipping_address_book_shipping_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Shipping_Location',
            new_name='Shipping_location',
        ),
    ]
