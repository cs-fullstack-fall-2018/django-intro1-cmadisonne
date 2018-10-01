from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def default (request):
    return HttpResponse("This is a bad request. Use one of the other routes.")

def kenn (request):
    return HttpResponse("This is Kenn.")

def language (request):
    return HttpResponse("My favorite language is Java Script (for now).")

def system (request):
    return HttpResponse("My favorite system is NPM (for now).")

def IDE (request):
    return HttpResponse("My favorite IDE to use is static web.")