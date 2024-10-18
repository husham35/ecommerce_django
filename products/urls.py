from django.urls import path
from .views import product_list, product_list_admin, add_product, edit_product, delete_product, product_details

urlpatterns = [
    path('', product_list, name='product_list'),  # Public product list
	path('products-list', product_list_admin, name='products-list-admin'),
    path('add/', add_product, name='add_product'),  # Admin only
	path('<int:product_id>/', product_details, name='product_details'),
    path('<int:product_id>/edit/', edit_product, name='edit_product'),  # Admin only
    path('<int:product_id>/delete/', delete_product, name='delete_product'),  # Admin only
]
