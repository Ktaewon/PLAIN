from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Melody(models.Model):
    owner = models.ForeignKey(User, related_name='melody', blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    img = models.ImageField(null=True, upload_to="melody/img/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    hashtags = TaggableManager()
    myInstrument = models.TextField()
    needInstrument = models.TextField(null=True, blank=True)
    audio = models.FileField(null=False, upload_to="melody/audio/", blank=False)
    def __str__(self):
        return f'[{self.pk}]{self.title}'