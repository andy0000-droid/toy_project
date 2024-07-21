from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def func(request):
    return HttpResponse(request, "<h1> This is mainpage </h1>")
