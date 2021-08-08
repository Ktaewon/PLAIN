from django.db import models
from django.contrib.auth.models import User
from Melody.models import Melody



# Create your models here.


class Comment(models.Model):
    Comment_body = models.CharField(max_length=200)
    Comment_date = models.DateTimeField()
    Comment_owner = models.ForeignKey(User, related_name='comment_owner', on_delete=models.CASCADE)
    Comment_post = models.ForeignKey(Melody, related_name='comment_post', on_delete=models.CASCADE)
