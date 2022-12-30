# Generated by Django 4.0.7 on 2022-11-23 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('james', '0007_rename_lesseeregister_register_delete_james_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='james',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Phone_number', models.CharField(max_length=30)),
                ('Country', models.CharField(max_length=30)),
                ('Email_id', models.CharField(max_length=40)),
                ('Username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=10)),
                ('Status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='lessorregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Phone_number', models.CharField(max_length=30)),
                ('Company_name', models.CharField(max_length=30)),
                ('Company_profile', models.FileField(upload_to='')),
                ('Country', models.CharField(max_length=40)),
                ('Email_id', models.CharField(max_length=40)),
                ('Username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=10)),
                ('Status', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameModel(
            old_name='register',
            new_name='lesseeregister',
        ),
    ]
