from django.shortcuts import render

from .models import Feedback

def feedback(req):
	return render(req,"feedback.html")

def feedTask(req):
    if req.method=="POST":
        n=req.POST.get('nm')
        c=req.POST.get('cn')
        e=req.POST.get('em')
        s=req.POST.get('sugg')
        ob=Feedback(name=n,contact=c,email=e,suggestion=s)
        ob.save()
    return render(req,"fd.html")
