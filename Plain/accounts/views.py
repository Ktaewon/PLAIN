from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import user

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('')
    return render(request, 'signup.html')
def create(request):
    new_user=user()
    new_user.email=request.POST['email']
    new_user.nickname=request.POST['nickname']
    new_user.genre=request.POST['genre']
    new_user.instrument=request.POST['instrument']
    new_user.save()
def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')