from django.urls import path
from . import views

# URL Conf
urlpatterns = [
	path('', views.index),
	path('contact-us', views.contact_us),
]
