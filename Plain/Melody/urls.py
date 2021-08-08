from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.melody),
    path("uploads/", views.upload_melody, name="upload")
]