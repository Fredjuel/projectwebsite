# Generated by Django 4.0.7 on 2022-11-26 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('james', '0014_alter_upload_container_condition_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='Status',
            field=models.BooleanField(default=False),
        ),
    ]