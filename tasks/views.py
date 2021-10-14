from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
tasks=[]

# Create your views here.
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority=forms.IntegerField(label="Priority",min_value=1,max_value=3)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request,"index.html",{
        "tasks":tasks
    })
def add(request):
    if request.method=="POST":
          form=NewTaskForm(request.POST)
          if form.is_valid():
              task=form.cleaned_data["task"]
              tasks.append(task)
              return HttpResponseRedirect(("index"))
          else:
              return render(request,"add.html",{
                  "form":form
              })

    return render(request,"add.html",{
        "form":NewTaskForm()
    })