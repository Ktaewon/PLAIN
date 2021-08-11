from django.db.models.expressions import Value
# from Plain.Melody.views import default
from django.db import models
from django.db.models.fields import TextField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, company_name, phone, password=None):
        if not email:
            raise ValueError("email is required")
        if not company_name:
            raise ValueError("company name is required")
        if not phone:
            raise ValueError("please provide an active phone number")
        user = self.model(
            email = self.normalize_email(email), 
            company_name = company_name,
            phone = phone
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self, email, company_name, phone, password=None):
        user = self.create_user(
            email = email,
            company_name= company_name,
            phone = phone,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address", max_length=60, unique=True)
    company_name = models.CharField(verbose_name="company name", max_length=200, unique=True)
    phone = models.CharField(max_length=20, verbose_name="company phone")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="date joined")
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['company_name', 'phone']
    objects= MyUserManager()
    def __str__(self):
        return self.company_name
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
# class UserManager(BaseUserManager):
#     def create_user(self, name, email, nickname, genre, instrument, password=None):
#         if not name:
#             raise ValueError('must have user Id')
#         if not email:
#             raise ValueError('must have user email')
#         user = self.model(
#             name=name,
#             email=self.normalize_email(email),
#             nickname=nickname,
#             genre=genre,
#             instrument=instrument,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, name, email, password):
#         user = self.create_user(
#             name=name,
#             email=self.normalize_email(email),
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user

# class User(AbstractBaseUser):
#     objects = UserManager()
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=255,unique=True,)
#     nickname=models.CharField(max_length=20, blank=True, null=False)
#     genre=models.CharField(max_length=20, blank=True)
#     instrument=models.TextField()
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     USERNAME_FIELD = 'name'
#     REQUIRED_FIELDS = ['email','nickname','genre', 'instrument']
#     def __str__(self):
#         return self.name
    
# def has_perm(self, perm, obj=None):
#     return True

# def has_module_perms(self, app_label):
#     return True

# @property
# def is_staff(self):
#     return self.is_admin