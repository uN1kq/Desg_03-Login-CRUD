from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):

    #Creation of Basic User
    def create_user(self, username, email, mobileno, password=None, **extra_fields):
        if not username:
            raise ValueError('The UserName field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        if not mobileno:
            raise ValueError('The Mobile Number field must be set')     
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, mobileno=mobileno, **extra_fields)
        user.set_password(password)     
        user.save(using=self._db)
        return user
    

    #Creation of Super User
    def create_superuser(self, username, email, mobileno, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True.')
        return self.create_user(username, email, mobileno, password, **extra_fields)



#Fields for Custom User Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    firstName = models.CharField(max_length=30, blank=True)
    lastName = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    mobileno = models.CharField(max_length=15, unique=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'mobileno']

    objects = CustomUserManager()


    def __str__(self):
        return self.username