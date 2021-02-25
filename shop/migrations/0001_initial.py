# Generated by Django 3.0.5 on 2021-02-25 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='book/')),
                ('Book_Name', models.CharField(max_length=100)),
                ('Book_Description', models.CharField(max_length=500)),
                ('Author', models.CharField(max_length=150)),
                ('Category', models.CharField(max_length=40)),
                ('Price', models.IntegerField()),
                ('Seller_Name', models.CharField(max_length=100)),
                ('Seller_Email', models.EmailField(max_length=254)),
                ('Seller_Phone', models.IntegerField()),
                ('otp', models.IntegerField()),
                ('phone_verified', models.BooleanField(default='False')),
                ('sold', models.BooleanField(default='False')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product/')),
                ('Product_Name', models.CharField(max_length=100)),
                ('Product_Description', models.CharField(max_length=500)),
                ('Price', models.IntegerField()),
                ('Seller_Name', models.CharField(max_length=100)),
                ('Seller_Email', models.EmailField(max_length=254)),
                ('Seller_Phone', models.IntegerField()),
                ('otp', models.IntegerField()),
                ('phone_verified', models.BooleanField(default='False')),
                ('sold', models.BooleanField(default='False')),
            ],
        ),
    ]
