from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.melody),
    path("uploads/", views.upload_melody, name="upload"),
    path("detail/<str:id>", views.detail, name="detail"),
    #path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    #path('tag/<str:tag>', views.TaggedObjectLV.as_view(), 
    #    name='tagged_object_list'),
    path("default/",views.default,name="default"),

    path('comment/<str:id>', views.comment, name='comment'),
    path('comment/delete/<str:id>', views.comment_delete, name='comment_delete'),
    # Like
    path('like/<int:id>', views.post_like, name='post_like'),
]   

