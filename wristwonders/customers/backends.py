from typing import Any
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http import HttpRequest
from .models import User

class CustomBackend(ModelBackend):
    def authenticate(self,request,email=None,password =None,**kwargs):
        try:
            user = User.objects.get(email = email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None 