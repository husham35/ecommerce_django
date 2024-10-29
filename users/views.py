from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
# fetch customers
@staff_member_required
def customers(request):
    customers = User.objects.filter(is_staff=False)
    return render(request, 'users/customers.html', {'customers': customers})

# fetch one customer
def customer(request, customer_id):
    customer = get_object_or_404(User, id=customer_id, is_staff=False)
    if request.user.is_authenticated and request.user.is_staff:
        return render(request, 'users/customer_details.html', {'customer': customer})
    return render(request, 'users/customer_profile.html', {'customer': customer})


# fetch one customer
@staff_member_required
def delete_customer(request, customer_id):
    customer = get_object_or_404(User, id=customer_id, is_staff=False)
    print(customer)
    if request.method == 'POST':
        customer.delete()
        messages.success(request, 'Customer deleted successfully')
        return redirect('customers')
    return render(request, 'users/customers.html', {'customer': customer})

