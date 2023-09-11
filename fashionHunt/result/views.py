from django.shortcuts import render
from django.http import HttpResponse
from .models import Result

def result(req):
	return render(req,"result.html")

def resTask(req):
	if req.method=="POST":
		sn=req.POST.get('sno')
		n=req.POST.get('name')
		typ=req.POST.get('type')
		tm=req.POST.get('team')
		s=req.POST.get('sts')
		pr=req.POST.get('prm')
		ob=Result(sno=sn,cname=n,type=typ,team=tm,status=s,prize=pr)
		ob.save()
	return HttpResponse('Result added successfully')

def resShow(req):
	ob=Result.objects.all()
	return render(req,"resShow.html",{'data':ob})