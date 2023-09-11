from django.db import models

class Result(models.Model):
	sno=models.CharField(max_length=15)
	cname=models.CharField(max_length=70)
	type=models.CharField(max_length=50)
	team=models.CharField(max_length=50)
	status=models.CharField(max_length=50)
	prize=models.CharField(max_length=50)