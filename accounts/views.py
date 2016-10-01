from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect, render
from django.conf import settings
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from models import MyUser
import os
import sys

def homepage(request):
	pass

def login_user(request):
	c={}
	c.update(csrf(request))
	"""return render_to_response('accounts/login.html',csrf_token = c)"""
	return render(request,'accounts/login.html',c)

def auth_login(request):
	username = request.POST.get('username')
	passw = request.POST.get('password')
	u= authenticate(username = username, password = passw)

	if u is not None:
		login(request,u)

		data = {
			'user' : u
		}

		return render(request, 'accounts/successful_login.html', data)

	else:
		data = {
			'message' : 'Error! Invalid Usename or Password'
		}
		return render(request, 'accounts/login.html', data)

def logout_user(request):
	logout(request.user)
	data = {
		'message' : 'Successfully Logged Out!'
	}
	return render(request, 'accounts/logout.html', data= data)

def leaderboard(request):
	users= MyUser.objects.all().order_by('score')

	lead={}
	for user in range(len(users)):
		lead[user] = {
			'username' : users[user].username,
			'score' : users[user].score
		}

	data = {
		'leaderboard' : lead,
		'message' : 'messages'
	}
	return render(request , 'accounts/leaderboard.html',data=data)

def index(request):
	return HttpResponse('hi')