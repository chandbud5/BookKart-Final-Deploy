from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.db.models import Q
from .models import product, book
import time, os, random
from twilio.rest import Client
# Create your views here.

def home(request):
	b = book.objects.all().order_by('-id')[:3]
	prod = product.objects.all().order_by('-id')[:3]
	print(b)
	print(type(b))
	return render(request, 'index.html', {'books':b, 'products': prod})

def about(request):
    return render(request, 'about.html')

def prod(request):
	num = request.GET.get('id')
	print(num)
	obj = product.objects.get(id = num)
	return render(request, 'product.html', {'book_obj': obj})

def prod_b(request):
	num = request.GET.get('id')
	print(num)
	obj = book.objects.get(id = num)
	return render(request, 'product_b.html', {'book_obj': obj})

def search(request):
	keyword = request.GET.get('query')
	print(keyword)

	if keyword != "":
		empty = False
		no_books = False
		no_product = False
		b_obj = book.objects.filter(Q(Book_Name__icontains=keyword) | Q(Author__icontains=keyword) | Q(Book_Description=keyword)).order_by('-id')
		prod = product.objects.filter(Q(Product_Name__icontains=keyword) | Q(Product_Description__icontains=keyword)).order_by('-id')
		
		if len(b_obj) == 0 and len(prod) == 0:
			empty = True
		return render(request, 'search.html', {'book_obj':b_obj, 'product':prod, 'empty':empty})
	else:
		messages.info(request, "alert()")
		return redirect('/')

def login(request):
	return render(request, 'login.html')

def profile(request):
	return render(request, 'profile.html')

def register(request):
	return render(request, 'registration.html')

def signup(request):
	if request.method == 'POST':
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		e_mail = request.POST.get('email')
		uname = request.POST.get('uname')
		pwd = request.POST.get('pass')
		re_pwd = request.POST.get('re_pass')

		already = User.objects.filter(email = e_mail).exists()
		if not already:
			bool_incorrect = False
			if pwd==re_pwd:
				user = User.objects.create_user(username=uname, password=pwd, email=e_mail,
					first_name=fname, last_name=lname)
				user.save()
				messages.info(request, "Registration Successful please login")
				return redirect('/login/')
			else:
				bool_incorrect = True
				messages.info(request, 'Password does not match')
				return render(request, 'registration.html')
		else:
			messages.info(request, 'User Already Exist')
			return redirect('/login')

def authenticate(request):

	if request.method == 'POST':
		uname =  request.POST.get("uname")
		pasw = request.POST.get("pass")

		user = auth.authenticate(username=uname, password=pasw)

		if user is not None:
			print("LOgin Successful")
			auth.login(request, user)
			return redirect('/')
		else:
			messages.info(request, "Invalid Credential")
			return redirect('/login/')

	else:
		return redirect('/login/')

def logout(request):
	auth.logout(request)
	print("logout Successful")
	return redirect('/')

def sell(request):
	return render(request, 'add_product.html')

def sell_b(request):
	return render(request, 'add_product_b.html')

def verify(request):
	return render(request, 'verify.html')

def verify_b(request):
	return render(request, 'verify_b.html')

def add_product(request):
	if request.method == 'POST':
		bname = request.POST.get('bname')
		bdesc = request.POST.get('bdesc')
		aname = request.POST.get('aname')
		category = request.POST.get('category')
		price = request.POST.get('price')
		phone = request.POST.get('phone')
		item = request.POST.get('item')
		e_mail = request.POST.get('email')
		image = request.FILES['productimg']
				
		account_sid = 'AC23ed0a12c44791bf16cf0a02fcdc2efe'
		auth_token = '4ffecb8caecb7df8110ff3c2b68fcc41'
		client = Client(account_sid, auth_token)
		print("Sending message")

		otp = random.randint(1000,9999)
		print(otp)
		message = client.messages \
		    .create(
		         body='Your OTP for verification on BookKart is '+ str(otp),
		         from_='+19285639513',
		         to="+91"+phone)

		print(message.sid)
		if item == "Stationary Item":
			prod = product.objects.create()
			prod.Product_Name = bname
			prod.Product_Description = bdesc
			prod.Price = price
			prod.Seller_Name = request.user.first_name + " " + request.user.last_name
			prod.Seller_Email = e_mail
			prod.Seller_Phone = phone
			prod.image = image
			prod.save()
			return redirect('/')
		else:
			b = book.objects.create()
			b.Book_Name = bname
			b.Book_Description = bdesc
			b.Author = aname
			b.Category = category
			b.Price = price
			b.Seller_Name = request.user.first_name + " " + request.user.last_name
			b.Seller_Email = e_mail
			b.Seller_Phone = phone
			b.image = image
			b.save()
			return redirect('/')
	else:
		return redirect('/sell/')

def add_product_b(request):
	if request.method == 'POST':
		bname = request.POST.get('bname')
		bdesc = request.POST.get('bdesc')
		aname = request.POST.get('aname')
		category = request.POST.get('category')
		price = request.POST.get('price')
		phone = request.POST.get('phone')
		item = request.POST.get('item')
		e_mail = request.POST.get('email')
		image = request.FILES['productimg']

		if item == "Stationary Item":
			prod = product.objects.create()
			prod.Product_Name = bname
			prod.Product_Description = bdesc
			prod.Price = price
			prod.Seller_Name = request.user.first_name + " " + request.user.last_name
			prod.Seller_Email = e_mail
			prod.Seller_Phone = phone
			prod.image = image
			prod.save()
			return redirect('/')
		else:
			b = book.objects.create()
			b.Book_Name = bname
			b.Book_Description = bdesc
			b.Author = aname
			b.Category = category
			b.Price = price
			b.Seller_Name = request.user.first_name + " " + request.user.last_name
			b.Seller_Email = e_mail
			b.Seller_Phone = phone
			b.image = image
			b.save()
			return redirect('/')
	else:
		return redirect('/sell_b/')