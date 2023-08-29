from django.shortcuts import render
from django.http import HttpResponse
def wish (request):
    return HttpResponse("hi da thambi django")
def one (request):
    return HttpResponse("<h1>one<h1>")
def two(request):
    return HttpResponse("<h1>two<h1>")
def three (request):
    return HttpResponse("<h1>three<h1>")
