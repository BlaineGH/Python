from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from random import randint
from datetime import datetime
from .models import User
import bcrypt
from django.contrib import messages

def index(request):
	return render(request, 'loginandregistration/index.html')

def success(request):
	context = {
		'username' : User.objects.get(id=request.session['id']).firstname
	}
	return render(request, 'loginandregistration/success.html', context)

def register(request):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	else:
		hashword = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		User.objects.create(firstname=request.POST['first_name'],lastname=request.POST['last_name'],email=request.POST['email'],password=hashword)
		user = User.objects.get(email=request.POST['email'])
		request.session['id'] = user.id
		return redirect('/success')

def login(request):
	errors = User.objects.login_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	else:
		user = User.objects.get(email=request.POST['email'])
		request.session['id'] = user.id
		return redirect('/success')