# Generated by Django 4.0.7 on 2022-11-24 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('james', '0009_register_delete_james_delete_lesseeregister_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='Company_name',
            new_name='Country',
        ),
        migrations.RemoveField(
            model_name='register',
            name='Company_address',
        ),
    ]