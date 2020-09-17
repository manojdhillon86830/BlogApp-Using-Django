from django.db import models
# Create your models here.
class Blog(models.Model):
    name=models.CharField(max_length=100)
    Gmail=models.EmailField()
    content=models.CharField(max_length=5000)

class Resister(models.Model):
    username=models.CharField(max_length=100)
    Gmail=models.EmailField()  
    password=models.CharField(max_length=50, null=True)