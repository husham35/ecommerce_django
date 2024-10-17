# from django.shortcuts import render, redirect
# from django.http import HttpResponse

# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.decorators import login_required
# from django.contrib.admin.views.decorators import staff_member_required
# from django.http import HttpResponseRedirect, HttpResponse



# from django.contrib.auth.decorators import login_required

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout

from allauth.account.views import LoginView

# Create your views here
# def login_page(request):
#     return render(request, "accounts/login.html")

class CustomLoginView(LoginView):
    def get_success_url(self):
        user = self.request.user
        if user.is_staff:
            return '/accounts/staff_dashboard/'
        else:
            return '/home/'

def register_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after sign-up
            return redirect('home')  # Redirect to homepage after signup
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {'form': form})

# Staff dashboard view
@staff_member_required
def staff_dashboard(request):
    return render(request, 'accounts/staff_dashboard.html')


def forgot_password(request):
    return render(request, "accounts/forgot_password.html")

# def _password(request):
# 	return render(request, "accounts/forgot_password.html")

@login_required
def after_login_redirect(request):
    if request.user.is_staff:
        return 'dashboard' # Change 'admin_dashboard' to the correct URL name for your custom admin page
    else:
        return 'home'  # Change 'user_dashboard' to the correct URL for normal users
