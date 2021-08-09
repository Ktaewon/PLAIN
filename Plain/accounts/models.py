from django.db import models
from django.db.models.fields import TextField
# Create your models here.

class user(models.Model):
    email=models.CharField(max_length=30)
    nickname=models.CharField(max_length=20)
    genre=models.CharField(max_length=20)
    instrument=models.TextField()