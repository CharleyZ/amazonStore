# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Image,User
from .forms import UserForm,LoginForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
	user_name = "not logged in"
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user_name = form.cleaned_data["name"]
			request.session['user_name'] = user_name
			return redirect(user)
	else:
		form = LoginForm()
	return render(request,'index.html',{'user_name':user_name,'form':form})



def thankyou(request):
	return render(request,'thankyou.html')

def user(request):
	user_all = User.objects.all()
	paginator = Paginator(user_all, 5)
	page = request.GET.get('page')
	user_name = "new user"
	try:
		user_list = paginator.page(page)
	except PageNotAnInteger:
		user_list = paginator.page(1)
	except EmptyPage:
		user_list = paginator.page(paginator.num_pages)


	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			user = User()
			user.name = form.cleaned_data['name']
			user_name = user.name
			user.email = form.cleaned_data['email']
			user.password = form.cleaned_data['password']
			user.isSeller = form.cleaned_data['isSeller']
			user.save()

	else:
		form = UserForm()
		if request.session.has_key('user_name'):
			user_name = request.session['user_name']
	
	return render(request,'user.html',{'user_list':user_list,'form':form,'user_name':user_name})

