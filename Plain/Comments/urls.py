from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.sub_page),
    #path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    #path('tag/<str:tag>', views.TaggedObjectLV.as_view(), 
    #    name='tagged_object_list'),
]