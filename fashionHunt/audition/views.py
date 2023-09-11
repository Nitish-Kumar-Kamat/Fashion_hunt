from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Audition_Reg

def audi(req):
	return render(req,"audireg.html")

def audiTask(req):
    if req.method=="POST":
        n=req.POST.get('name')
        e=req.POST.get('email')
        d=req.POST.get('date')
        p=req.POST.get('place')
        img=req.FILES.get('fimg')
        ob=Audition_Reg(name=n,email=e,date=d,place=p,image=img)
        ob.save()
    return HttpResponse("Audition registration successfully")


