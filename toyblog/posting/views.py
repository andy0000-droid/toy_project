from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def func(request):
    return HttpResponse("<h1> This is postpage </h1>")  # Testing code
    # return render(request)
