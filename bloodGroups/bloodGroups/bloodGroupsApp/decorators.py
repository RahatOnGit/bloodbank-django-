from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
          return redirect('home')
        
        return view_func(request, *args, **kwargs)
    
    return wrapper_func



def admin_only(view_func):
   def wrapper_func(request, *args, **kwargs):
      group = None
      if request.user.groups.exists():
         group = request.user.groups.all()[0].name

      if group == 'user_group':
         return redirect('home')
      if group == 'admin':
         return  view_func(request, *args, **kwargs)
   return wrapper_func