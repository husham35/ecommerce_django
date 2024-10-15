from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
def index(response):
	return render(response, "home/homepage.html")

def say_hello(request):
	return HttpResponse('Hello Django')

def contact_us(request):
	return HttpResponse('Contact us page')