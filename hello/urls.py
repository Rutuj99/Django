from django.urls import path 
from . import views
urlpatterns=[
    path("hello",views.index, name="index"),
    path("rutuj",views.rutuj,name="rutuj"),
    path("baba",views.baba,name="baba"),
    path("<str:name>",views.greet,name="greet"),
    path("",views.page,name="page"),
    path("mum",views.yash,name="yash")
]