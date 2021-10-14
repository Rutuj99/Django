from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("heloool")

def page(request):
    return render(request ,"index.html")

def rutuj(request):
    return HttpResponse("hey rutuj have make this days count")

def baba(request):
    return HttpResponse("I will make you proud")

def greet(request,name):
    return render(request,"greet.html",{
        "name":name.capitalize()
    })
def yash(request):
    return HttpResponse("sweet ok cook as per your choise")
