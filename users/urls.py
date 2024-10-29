from django.urls import path
from .views import customers, customer, delete_customer

urlpatterns = [
	path('', customers, name='customers'),
	path('<int:customer_id>', customer, name='customer'),
	path('delete/<int:customer_id>', delete_customer, name='delete_customer'),
]