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

    
    likes = models.ManyToManyField(User, through='Like', through_fields=('melody', 'user'), related_name="likes")

    def __str__(self):
        return f'[{self.pk}]{self.title}'


class Joiner(models.Model):
    body = models.TextField(max_length=500)
    positon=models.TextField(max_length=500,null=True)  #position
    pub_date = models.DateTimeField('data published')
    writer = models.ForeignKey(User , on_delete = models.CASCADE)  #user랑 연결
    post = models.ForeignKey(Melody, on_delete = models.CASCADE)     #melody 게시물이랑 연결
    audio = models.FileField(null=False, upload_to="melody/audio/joiner", blank=False)  #오디오도!
    #이부분 모르겠음 upload_to 가 뭐임 이거랑 form에서 음악 받아오는부분
    
   

'''joiner가 comment랑 똑같은 기능을 하는 객체임!!!!!! 
이밑으로는 아직 사용하지 않았음 ,,
'''
class Comment(models.Model):
    Comment_body = models.CharField(max_length=200)
    Comment_date = models.DateTimeField()
    Comment_owner = models.ForeignKey(User, related_name='comment_ownerr', on_delete=models.CASCADE)
    Comment_post = models.ForeignKey(Melody, related_name='comment_postt', on_delete=models.CASCADE)

class Like(models.Model):
    melody = models.ForeignKey(Melody, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    followee = models.ForeignKey(User, related_name='followee', on_delete=models.CASCADE)




