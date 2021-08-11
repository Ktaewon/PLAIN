from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.melody),
    path("uploads/", views.upload_melody, name="upload"),
    path("detail/<str:id>", views.detail, name="detail"),
    path('comment/<str:id>', views.createcomment, name='comment'),
    path("default/<str:id>", views.detail, name="default"),

    #path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    #path('tag/<str:tag>', views.TaggedObjectLV.as_view(), 
    #    name='tagged_object_list'),
    #path("default/",views.default,name="default"),
]