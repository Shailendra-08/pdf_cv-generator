from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone  = models.CharField(max_length=20)
    summary = models.TextField(max_length=20)
    degree = models.CharField(max_length=20)
    school = models.CharField(max_length=20)
    university = models.CharField(max_length=20)
    previous_work = models.TextField(max_length=2000)
    skills = models.CharField(max_length=1000)
    
    
    
    
