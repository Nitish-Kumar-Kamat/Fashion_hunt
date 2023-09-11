from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Category

def category(req):
	return render(req,"category.html")

def categoryTask(req):
    if req.method=="POST":
        c=req.POST.get('tcid')
        nm=req.POST.get('tname')
        if len(req.FILES)!=0:
            img=req.FILES['timg']
        dum=Category(cid=c,cname=nm,image=img)
        dum.save()
    return HttpResponse("Category inserted")

def catshow(req):
    s=Category.objects.all()
    data={
        'sk':s
    }
    return render(req,"catshow.html",data)
