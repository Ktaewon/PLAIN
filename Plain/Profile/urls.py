from django.urls import path
from django.urls.resolvers import URLPattern
from . import path
from django.conf.urls.static import static

urlpatterns = [
    path('profile/',views.profile,name='profile')
    
]