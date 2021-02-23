# Generated by Django 3.1.1 on 2021-02-23 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Membername', models.CharField(max_length=100)),
                ('Designation', models.CharField(max_length=500)),
                ('photo', models.ImageField(upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Itemname', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
                ('photo', models.ImageField(upload_to='photos/')),
            ],
        ),
    ]
