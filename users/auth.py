from curses import wrapper
from django.shortcuts import redirect


# to check if the user is logged in or not


def unauthenticated_user(view_function):
    def wrapper_function(request, *args, **kwrgs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_function(request, *args, **kwrgs)
    return wrapper_function


# give access to user pages if request comes from user
# if request is from normal user, redirect to user dashboard

def admin_only(view_function):
    def wrapper_function(request, *args, **kwrgs):
        if request.user.is_staff:
            return view_function(request, *args, **kwrgs)
        else:
            return redirect('/')
    return wrapper_function
