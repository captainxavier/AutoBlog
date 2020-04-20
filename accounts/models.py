from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime


def upload_profile_pic(instance, time):
    time=datetime.datetime.now()
    file_path = 'profile_pic/{username}/{name}-{time}'.format(
        username=str(instance.username), name="XAB",   time=str(time)

    )
    return file_path

class MyAccountManager(BaseUserManager):
    def create_user(self, email,first_name,last_name, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not first_name:
            raise ValueError('Users must have a First Name')
        if not last_name:
            raise ValueError('Users must have a Surname')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,first_name, last_name, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name = last_name,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    profile_picture = models.ImageField(upload_to=upload_profile_pic, max_length=500,null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    objects = MyAccountManager()

    
    class Meta:
        db_table = 'accounts'
        verbose_name = ("Account")
        verbose_name_plural = ("Accounts")

    def __str__(self):
        return self.username

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True