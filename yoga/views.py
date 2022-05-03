from django.shortcuts import render,redirect
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')  

def login(request):
    return render(request,'login.html')

def index1(request):
    return render(request,'index1.html')