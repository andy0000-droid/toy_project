from django.contrib import admin
from django.urls import path, include
from . import views as write

urlpatterns = [
    path("", write.func),
]
