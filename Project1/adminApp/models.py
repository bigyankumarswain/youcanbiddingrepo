from django.db import models

class AdminModel(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    email =models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    contact=models.IntegerField(unique=True)
    image=models.ImageField(upload_to="AdminImage/")
