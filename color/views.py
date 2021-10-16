from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now=datetime.datetime.now()
    return render(request,"color.html",{
        "firstday":now.month==9 and now.day==26,
        "secondday":now.month==9 and now.day==27,
        "thirdday":now.month==9 and now.day==28,
        "fouthday":now.month==9 and now.day==29,
        "fifthday":now.month==9 and now.day==30,
        "sixthday":now.month==10 and now.day==1,
        "seventhday":now.month==10 and now.day==2,
        "eigthday":now.month==10 and now.day==3,
        "ninthday":now.month==10 and now.day==4
     
    })