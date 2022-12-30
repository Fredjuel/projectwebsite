# Generated by Django 4.0.7 on 2022-11-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Phone_number', models.CharField(max_length=30)),
                ('Company_name', models.CharField(max_length=30)),
                ('Company_address', models.CharField(max_length=40)),
                ('Username', models.CharField(max_length=30)),
                ('Email_id', models.CharField(max_length=40)),
                ('Password', models.CharField(max_length=10)),
                ('Status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Designation', models.CharField(max_length=20)),
                ('Picture', models.FileField(upload_to='')),
            ],
        ),
    ]
