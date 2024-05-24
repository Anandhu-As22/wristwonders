from typing import Any
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin,Group,Permission
from django.db import models

# Create your models here.

# model  for users

class UserManager(BaseUserManager):
    
    def create_user(self,email,username,password=None,**extra_fields):
        if not email:
            raise ValueError('The email field mustbe set')
        email =self.normalize_email(email)
        user = self.model(email=email,username=username,**extra_fields)
        user.set_password(password)
        user.save(using = self._db)

        return user
    def create_superuser(self,email,username,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        return self.create_user(email,username,password,**extra_fields)
    
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=300,unique=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff =models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name='customers_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customers_user_permissions_set', blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username','first_name','last_name']

    def __str__(self) -> str:
        return self.username
    


