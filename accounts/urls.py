from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# URL Conf

urlpatterns = [
	path('login', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
	path('logout', auth_views.LogoutView.as_view(), name='logout'),
	path('signup', views.register_page, name='signup'),
	path('forgot-password', views.forgot_password, name='forgot-password'),

]