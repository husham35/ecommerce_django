# from django.shortcuts import redirect

# class RedirectStaffMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Check if the user is authenticated and is staff
#         if request.user.is_authenticated and request.user.is_staff:
#             # If the user is on the login or profile page, redirect them
#             if request.path == '/user/dashboard/':
#                 return redirect('/admin/dashboard/')
#         return self.get_response(request)