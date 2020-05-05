from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self,email,name,password=None):
        """Create new user profile"""
        if not email:
            raise ValueError('User must have an email address') 

        email=self.normalize_email(email) #case sensitive,gmail hotmail, etc etc
        user=self.model(email=email,name=name)

        user.set_password(password) #password stored as hash not as original password,can't hack 
        user.save(using=self.db) 
        return user

    def create_superuser(self,email,name,password):
        """Create and save a superuser"""
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self.db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)


    """use and manage users"""
    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name'] 

    def get_full_name(self):
        return self.name 

    def get_short_name(self):
        return self.name 
    
    def __str__(self):
        return self.email 

    