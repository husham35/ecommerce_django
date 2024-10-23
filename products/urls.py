from django.urls import path
from .views import product_list, product_list_admin, add_product, edit_product, delete_product, product_details, category_list, add_category, category_details, edit_category, delete_category

urlpatterns = [
	# product
    path('', product_list, name='product_list'),  # Public product list
	path('products-list', product_list_admin, name='products-list-admin'), # Admin only
    path('add/', add_product, name='add_product'),  # Admin only
	path('<int:product_id>/', product_details, name='product_details'),
    path('<int:product_id>/edit/', edit_product, name='edit_product'),  # Admin only
    path('<int:product_id>/delete/', delete_product, name='delete_product'),  # Admin only
	# product category
    path('category-list', category_list, name='category-list'), # Admin only
    path('add-category/', add_category, name='add_category'),  # Admin only
	path('<int:category_id>/', category_details, name='category_details'),
    path('<int:category_id>/edit/', edit_category, name='edit_category'),  # Admin only
    path('<int:category_id>/delete/', delete_category, name='delete_category'),  # Admin only
]
