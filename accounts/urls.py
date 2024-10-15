from django.urls import path
from . import views

# URL Conf

urlpatterns = [
	path('login', views.login_page, name='login'),
	path('signup', views.register_page, name='signup'),
	path('forgot-password', views.forgot_password, name='forgot-password'),

]