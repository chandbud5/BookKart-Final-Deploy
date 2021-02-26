from django.db import models

# Create your models here.

class book(models.Model):
	image = models.ImageField(upload_to='book/')
	Book_Name = models.CharField(max_length=100)
	Book_Description = models.CharField(max_length=500)
	Author = models.CharField(max_length=150)
	Category = models.CharField(max_length=40)
	Price = models.IntegerField()
	Seller_Name = models.CharField(max_length=100)
	Seller_Email = models.EmailField()
	Seller_Phone = models.IntegerField()
	otp = models.IntegerField()
	phone_verified = models.BooleanField(default="False")
	sold = models.BooleanField(default="False")
	
class product(models.Model):
	image = models.ImageField(upload_to='product/')
	Product_Name = models.CharField(max_length=100)
	Product_Description = models.CharField(max_length=500)
	Price = models.IntegerField()
	Seller_Name = models.CharField(max_length=100)
	Seller_Email = models.EmailField()
	Seller_Phone = models.IntegerField()
	otp = models.IntegerField()
	phone_verified = models.BooleanField(default="False")
	sold = models.BooleanField(default="False")

class Payment_User(models.Model):
	Name = models.CharField(max_length=100, default="")
	Phone = models.IntegerField(default="")
	UPI_ID = models.CharField(max_length=100, default="")
	Email = models.EmailField(default="")