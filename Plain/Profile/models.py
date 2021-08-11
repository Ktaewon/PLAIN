from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.fields import TextField
from django.dispatch import receiver
from django.db.models.signals import post_save
