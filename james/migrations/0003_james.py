# Generated by Django 4.0.7 on 2022-11-22 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('james', '0002_lesseeregister_lessoregister_delete_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='james',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Phone_number', models.CharField(max_length=30)),
                ('Country', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=40)),
                ('Username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=10)),
                ('Status', models.BooleanField(default=False)),
            ],
        ),
    ]
