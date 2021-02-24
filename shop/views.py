from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import product, book
# Create your views here.

def home(request):
	return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def product(request):
	return render(request, 'add_product.html')

def login(request):
	return render(request, 'login.html')

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
				messages.info("Registration Successful please login")
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