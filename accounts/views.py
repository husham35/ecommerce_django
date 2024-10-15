from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here
def login_page(request):
	return render(request, "accounts/login.html")

def register_page(request):
	return render(request, "accounts/signup.html")

def forgot_password(request):
	return render(request, "accounts/forgot_password.html")

# def _password(request):
# 	return render(request, "accounts/forgot_password.html")
