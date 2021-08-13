from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')
def create(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            new_user=User.objects.create_user(request.POST['email'], password=request.POST['password1'])
            #new_user.email=request.POST['email']
            new_user.nickname=request.POST['nickname']
            new_user.genre=request.POST['genre']
            new_user.instrument=request.POST['instrument']
            new_user.save()
            return redirect('login')
def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        print(username, password)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("로그인 성공")
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')
def home(request):
        return render(request, 'home.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'home.html')

