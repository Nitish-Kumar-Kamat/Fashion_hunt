from django.db import models

class Audition_Reg(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    place=models.CharField(max_length=250)
    date=models.DateField()
    image=models.FileField(upload_to="media/Audition/")
