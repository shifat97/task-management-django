from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # Work with database
    # Transform data
    # Data pass
    # Https response / JSON response
    return HttpResponse("Welcome to the home page")

def contact(request):
    return HttpResponse("<h1 style='color:red;'>Welcome to contact page</h1>")

def show_task(request):
    return HttpResponse("<h1 style='color:blue'>Welcome to task page</h1>")