from django.shortcuts import render, get_object_or_404, redirect
from .models import Wishlist, WishlistItem
from products.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    
    # Check if the product is already in the wishlist
    if not WishlistItem.objects.filter(wishlist=wishlist, product=product).exists():
        WishlistItem.objects.create(wishlist=wishlist, product=product)
    
    return redirect('wishlist_view')  # Redirect to the wishlist view


@login_required
def remove_from_wishlist(request, product_id):
    wishlist = Wishlist.objects.get(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    WishlistItem.objects.filter(wishlist=wishlist, product=product).delete()
    return redirect('wishlist_view')


@login_required
def wishlist_view(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'wishlist': wishlist})



