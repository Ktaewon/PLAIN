from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login, name='login'),
    # path('create/', views.create, name='create'),
    path('admin/', admin.site.urls),
]
