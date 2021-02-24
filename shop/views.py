from django.shortcuts import render
from django.http import HttpResponse
from .models import user
# Create your views here.

def home(request):
	return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def login(request):
	return render(request, 'login.html')

def register(request):
	return render(request, 'registration.html')

def signup(request):
	name = request.POST.get('name')
	email = request.POST.get('email')
	phone = request.POST.get('phone')
	college = request.POST.get('college')
	faculty = request.POST.get('faculty')
	password = request.POST.get('pass')
	re_password = request.POST.get('re_pass')

	already = user.objects.filter(Email = email)

	if not already:
		if password==re_password:
			add_user = user.objects.create()
			add_user.Name = name
			add_user.Email = email
			add_user.phone = phone
			add_user.College = college
			add_user.Faculty = faculty
			add_user.password = password
			add_user.save()

		else:
			print("password does not match")
	else:
		print("User Already exists")

	return render(request, 'index.html')