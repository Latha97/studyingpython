from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    parts="calculations"
    return render(request,"home.html",{'obj':parts})
def operations(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    add=x+y
    div=x/y
    sub=x-y
    mul=x*y
    return render(request,"operations.html",{'addition':add,'division':div,'substraction':sub,'multiplication':mul})


