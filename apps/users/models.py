from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from .seo import CustomUserManager


class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username', max_length=50, unique=False)
    email = models.EmailField('email address', unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    is_Contentmaker = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = CustomUserManager()

    def __str__(self):
        return f'{self.email}'


class Reader(MyUser):
    name = models.CharField("user name", max_length=70, unique=False, null=False, blank=False)


class Contentmaker(MyUser):
    name = models.CharField("user name", max_length=70, unique=False, null=False, blank=False)



