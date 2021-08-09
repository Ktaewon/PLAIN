from django.db import models
from django.db.models.fields import TextField
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email=models.CharField(max_length=30, blank=True)
    nickname=models.CharField(max_length=20, blank=True)
    genre=models.CharField(max_length=20, blank=True)
    instrument=models.TextField()