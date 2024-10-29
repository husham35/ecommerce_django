from django.urls import path
from .views import product_list, product_list_admin, add_product, edit_product, delete_product, product_details, category_list, add_category, category_details, edit_category, delete_category

urlpatterns = [
	# product
    path('', product_list, name='product_list'),  # Public product list
	path('products-list', product_list_admin, name='products-list-admin'), # Admin only
    path('add/', add_product, name='add_product'),  # Admin only
	path('<int:product_id>/', product_details, name='product_details'), # customer view
	# path('<int:product_id>/', product_details, name='product_view'), # admin view
    path('edit/<int:product_id>', edit_product, name='edit_product'),  # Admin only
    path('delete/<int:product_id>', delete_product, name='delete_product'),  # Admin only
	
	# product category
    path('categories-list', category_list, name='categories-list'), # Admin only
    path('categories/add-category/', add_category, name='add_category'),  # Admin only
	path('categories/<int:category_id>/', category_details, name='category_details'),
    path('categories/edit/<int:category_id>/', edit_category, name='edit_category'),  # Admin only
    path('categories/delete/<int:category_id>/', delete_category, name='delete_category'),  # Admin only
]
