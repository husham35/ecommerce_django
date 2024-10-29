from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Product
from .forms import ProductForm
from .models import Category
from .forms import CategoryForm

# View for listing products (accessible to all users)
def product_list(request):
    # products = Product.objects.all()
    # Filter products to only show published ones
    products = Product.objects.filter(published=True)
    return render(request, 'products/product_list.html', {'products': products})
    # return HttpResponse('Hello')

# View for listing products (admin/staff users)
@staff_member_required
def product_list_admin(request):
    products = Product.objects.all()
    return render(request, 'products/product_list_admin.html', {'products': products})
    # return HttpResponse('Hello')

# Only admin users can add a product
@staff_member_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products-list-admin')
    else:
        form = ProductForm()
    return render(request, 'products/product_add.html', {'form': form})


# products details view for customers
def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user.is_authenticated and request.user.is_staff:
        return render(request, 'products/product_view.html', {'product': product})
    else:
        return render(request, 'products/product_details.html', {'product': product})
    # if request.method == 'POST':
    #     form = ProductForm(request.POST, request.FILES, instance=product)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('product_list')
    # else:
    #     form = ProductForm(instance=product)
    


# Only admin users can update a product
# @staff_member_required
# def product_view(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     return render(request,)


# Only admin users can update a product
@staff_member_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products-list-admin')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_edit.html', {'form': form})

# Only admin users can delete a product
@staff_member_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('products-list-admin')
    return render(request, 'products/product_confirm_delete.html', {'product': product})


# Product category
# View for listing products (accessible to all users)
@staff_member_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})
    # return HttpResponse('Hello')

# Only admin users can add a product
@staff_member_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categories-list')
    else:
        form = CategoryForm()
    return render(request, 'products/category_add.html', {'form': form})


# Only admin users can update a product
# @staff_member_required
def category_details(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'products/category_view.html', {'category': category}) # {'category': category})


# Only admin users can update a product
@staff_member_required
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            print('valid form')
            form.save()
            return redirect('categories-list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'products/category_edit.html', {'form': form})

# Only admin users can delete a product
@staff_member_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted successfully!')
        return redirect('categories-list')
    # return render(request, 'products/category_confirm_delete.html', {'category': category})
