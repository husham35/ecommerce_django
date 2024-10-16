from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm

from django.contrib.auth.decorators import login_required



# Create your views here
def login_page(request):
    return render(request, "accounts/login.html")

def register_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after sign-up
            return redirect('home')  # Redirect to homepage after signup
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {'form': form})

def forgot_password(request):
    return render(request, "accounts/forgot_password.html")

# def _password(request):
# 	return render(request, "accounts/forgot_password.html")
