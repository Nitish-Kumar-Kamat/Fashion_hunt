from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Registration

def reg(req):
    return render(req,"reg.html")

def regTask(req):
    if req.method=="POST":
        n=req.POST.get('name')
        e=req.POST.get('email')
        p=req.POST.get('pass1')
        m=req.POST.get('mobile')
        a=req.POST.get('address')
        img=req.FILES.get('fimg')
        ob=Registration(name=n,email=e,password=p,mobile=m,address=a,image=img)
        ob.save()
    return redirect("/signup/login/")

def login(req):
    return render(req,"log.html")

def loginTask(req):
    global rec
    if req.method=="POST":
        e=req.POST.get('email')
        p=req.POST.get('pass1')
        ob=Registration(email=e,password=p)
        rec=Registration.objects.filter(email=e,password=p)
        for i in rec:
            if(e==e and p==p):
                return redirect('/signup/audition/')
            else:
                return redirect('/signup/login/')
        return redirect('/signup/login/')


def audition(req):
    return render(req,"audition.html",{'rec':rec})
 

