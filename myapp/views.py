from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def khmer(request):
    return render(request, 'khmer.html')

def python(request):
    return render(request, 'python.html')

def java(request):
    return render(request, 'java.html')

def c(request):
    return render(request, 'c.html')

def cpp(request):
    return render(request, 'cpp.html')

def csharp(request):
    return render(request, 'csharp.html')

def login(request):
    return render(request, 'login.html')

# Create submenu of sidebar
def khmerMenu(request):
    return render(request, 'menu/khmerMenu.html')

def pythonMenu(request):
    return render(request, 'menu/pythonMenu.html')

def javaMenu(request):
    return render(request, 'menu/javaMenu.html')

def cMenu(request):
    return render(request, 'menu/cMenu.html')

def cppMenu(request):
    return render(request, 'menu/cppMenu.html')

def csharpMenu(request):
    return render(request, 'menu/csharpMenu.html')