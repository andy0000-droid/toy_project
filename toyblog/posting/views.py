from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def show(request, postid):
    """Function for show specific post"""
    return HttpResponse("<h1>" + str(postid) + " post page </h1>")


def main(request):
    """Function for show post mainpage"""
    return HttpResponse("<h1> Posting mainpage </h1>")


def write(request):
    """Function for show post writing page"""
    return HttpResponse("Post Writing page")
