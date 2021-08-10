
from django.shortcuts import render
from .models import profile

def mypage(request, pk):
    user = User.objects.get(pk=pk)
    if user.profile:
        profile = user.profile
        context = {'profile':profile}
        return render(request, 'Profile/profile.html', context)
    else:
        return render(request, 'Profile/profile.html', context)
# Create your views here.
