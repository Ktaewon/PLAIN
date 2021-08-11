from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('melody')
    return render(request, 'signup.html')
def create(request):
    new_user=User()
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
            return redirect('melody')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')