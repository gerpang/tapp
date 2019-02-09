from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate, login

def login_authenticate(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

    else:
        # Return an 'invalid login' error message.
        return HttpResponse('Invalid credentials')

def login_view(request):
    pass
