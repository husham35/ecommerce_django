from django.urls import path
from . import views

# URL Conf
urlpatterns = [
	path('', views.index, name='home'),
	path('contact-us', views.contact_us),
]
