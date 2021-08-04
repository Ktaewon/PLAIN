from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Melody(models.Model):
    owner = models.ForeignKey(User, related_name='melody', blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    img = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    hashtags = models.TextField()
    def __str__(self):
        return f'[{self.pk}]{self.title}'