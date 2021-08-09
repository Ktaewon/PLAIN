from django.db import models
from django.db.models.fields import TextField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, name, email, nickname, genre, instrument, password=None):
        if not name:
            raise ValueError('must have user email')
        if not email:
            raise ValueError('must have user email')
        user = self.model(
            name=name,
            email=self.normalize_email(email),
            nickname=nickname,
            genre=genre,
            instrument=instrument,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, nickname, genre, instrument, password):
        user = self.create_user(
            name=name,
            email=self.normalize_email(email),
            nickname=nickname,
            genre=genre,
            instrument=instrument,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255,unique=True,)
    nickname=models.CharField(max_length=20, blank=True)
    genre=models.CharField(max_length=20, blank=True)
    instrument=models.TextField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email','nickname','genre', 'instrument']
    def __str__(self):
        return self.name
    
def has_perm(self, perm, obj=None):
    return True

def has_module_perms(self, app_label):
    return True

@property
def is_staff(self):
    return self.is_admin