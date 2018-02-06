from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, "welcome.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def login(request):
    return render(request, "login.html")

def forgot_password(request):
    return render(request, "forgot_password.html")
