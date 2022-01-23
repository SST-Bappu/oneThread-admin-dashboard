from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils.timezone import now
# Create your models here.
class UserAccountManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email,password=password,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,**extra_fields):
        user = self.create_user(email,password,**extra_fields)
        
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class CustomUser(AbstractUser):
    username = models.CharField(max_length=255,unique=True,blank=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255,unique=True)
    secondaryEmail = models.EmailField(max_length=255,blank=True,null=True)
    contactNo = models.CharField(max_length=255,blank=True,null=True)
    gender = models.CharField(max_length=10,blank=True)
    bloodGroup = models.CharField(max_length=10,blank=True)
    location = models.CharField(max_length=60,blank=True)
    about = models.CharField(max_length=50,blank=True)
    birthDate = models.DateField(blank=True,default=now)
    is_staff = models.BooleanField(default=False)
    profileImage = models.ImageField(blank=True)
    salt = models.CharField(max_length = 50, blank=True)
    isVerified = models.BooleanField(default=False)
    createdAt = models.DateTimeField(default=now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name',]
    objects = UserAccountManager()
    
    def get_full_name(self):
        return self.first_name+self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

