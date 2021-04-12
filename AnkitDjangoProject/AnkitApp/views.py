from django.shortcuts import render
from django.http import HttpResponse
# from . import forms

# Create your views here.
def portfolio(request):
    return render(request, 'AnkitApp/portfolio.html')

def home(request):
    name = "Hello"
    return render(request, 'AnkitApp/login.html')
    # return HttpResponse("Hello, welcome to the Home Page of Nagato Uzumaki")


def about(request):
    return HttpResponse("This is all about Nagato and SixPathsPain")


def contact(request):
    return HttpResponse("contact Nagato here  ")