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

    path('comment/<str:melody_id>', views.comment, name='comment'),
    path('comment/delete/<str:comment_id>', views.comment_delete, name='comment_delete'),
    # Like
    path('like/<int:melody_id>', views.post_like, name='post_like'),
    path('chat/<str:melody_id>', views.chat, name="chat"),
]   

