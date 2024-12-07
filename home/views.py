from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product, Category

# Create your views here
def index(request):
	categories = Category.objects.all()
	return render(request, "home/homepage.html", {'categories': categories})

def say_hello(request):
	return HttpResponse('Hello Django')

def contact_us(request):
	return HttpResponse('Contact us page')