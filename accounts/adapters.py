# from allauth.account.adapter import DefaultAccountAdapter
# from django.shortcuts import resolve_url, redirect

# class CustomAccountAdapter(DefaultAccountAdapter):
#     def get_login_redirect_url(self, request):
#         print("custom adapter")
#         user = request.user
#         if user.is_staff:
#             return 'accounts/staff_dashboard'
#         else:
#             return 'home'
