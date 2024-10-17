from django.urls import path
from .views import product_list, add_product, edit_product, delete_product, product_details

urlpatterns = [
    path('', product_list, name='product_list'),  # Public product list
    path('add/', add_product, name='add_product'),  # Admin only
	path('<int:product_id>/', product_details, name='product_details'),
    path('<int:product_id>/edit/', edit_product, name='edit_product'),  # Admin only
    path('<int:product_id>/delete/', delete_product, name='delete_product'),  # Admin only
]
