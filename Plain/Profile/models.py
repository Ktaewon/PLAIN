from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.fields import TextField
from django.dispatch import receiver
from django.db.models.signals import post_save

class profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=40, blank=True)
    genre = models.TextField(blank=True)
    position = models.TextField(blank=True)
    profile_photo = models.ImageField(
        blank=True,
        upload_to= 'profile/images',
        format='JPEG'
 
    )

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
# Create your models here.
