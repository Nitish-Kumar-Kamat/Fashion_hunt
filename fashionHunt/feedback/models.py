from django.db import models

class Feedback(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    suggestion=models.CharField(max_length=250)
   
