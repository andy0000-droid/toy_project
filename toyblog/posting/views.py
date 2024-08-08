from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def func(request, postid):
    return HttpResponse("<h1>" + str(postid) + " post page </h1>")


def main(request):
    return HttpResponse("<h1> Posting mainpage </h1>")
