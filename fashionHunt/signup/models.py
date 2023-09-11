from django.db import models

class Registration(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    mobile=models.CharField(max_length=20)
    address=models.CharField(max_length=250)
    image=models.FileField(upload_to="media/Registration/")
