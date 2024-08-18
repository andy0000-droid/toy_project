from django.contrib import admin
from django.urls import path, include
from . import views as post

urlpatterns = [
    path("", post.main, name="post"),
    path("<int:postid>/", post.show),
    path("write/", post.write, name="write"),
]
