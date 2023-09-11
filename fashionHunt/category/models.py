from django.db import models

class Category(models.Model):
    cid=models.IntegerField()
    cname=models.CharField(max_length=50)
    image=models.FileField(upload_to="media/Category/")

