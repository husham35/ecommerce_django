from django.dispatch import receiver
from allauth.account.signals import user_logged_in
from django.shortcuts import redirect
from django.urls import reverse

@receiver(user_logged_in)
def redirect_based_on_user_type(request, user, **kwargs):
    # Check if the user is staff and redirect accordingly
    print(f"Signal triggered for user: {user.username}")  # Debugging print statement

    # Check if the user is staff and redirect accordingly
    if user.is_staff:
        print("User is staff, redirecting to admin dashboard.")  # Debugging print statement
        return redirect('/admin-dashboard/')
    else:
        print("User is not staff, redirecting to user dashboard.")  # Debugging print statement
        return redirect('/user-dashboard/')
