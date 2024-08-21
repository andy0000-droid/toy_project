from django.urls import path
from . import views as post

urlpatterns = [
    path("", post.main, name="post"),
    path("<int:postid>/", post.show),
    path("write/", post.write, name="write"),
]
