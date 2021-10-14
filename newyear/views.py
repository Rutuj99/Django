import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    now=datetime.datetime.now()
    return render(request,"index.html",{
       "newyear":now.month==10 and now.day==8

   })
  