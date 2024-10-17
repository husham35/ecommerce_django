from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Product
from .forms import ProductForm

# View for listing products (accessible to all users)
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
    # return HttpResponse('Hello')

# Only admin users can add a product
@staff_member_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})


# Only admin users can update a product
# @staff_member_required
def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # if request.method == 'POST':
    #     form = ProductForm(request.POST, request.FILES, instance=product)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('product_list')
    # else:
    #     form = ProductForm(instance=product)
    return render(request, 'products/product_details.html', {'product': product}) # {'product': product})


# Only admin users can update a product
@staff_member_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form})

# Only admin users can delete a product
@staff_member_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})
