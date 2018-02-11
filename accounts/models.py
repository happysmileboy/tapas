from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', default=False)
        extra_fields.setdefault('is_staff', default=False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', unique=True)
    username = models.CharField(verbose_name='username', max_length=30)
    password = models.CharField(max_length=128, verbose_name='비밀번호')
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(verbose_name='active', default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


class EmailConfirm(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='email_confirm',
        on_delete=models.CASCADE,
    )
    key = models.CharField(max_length=60)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    nickname = models.CharField(max_length=20, verbose_name='닉네임')
    image = models.ImageField(
        upload_to='profile/%Y/%m/%d/',
        blank=True,
        null=True,
    )
    birth_day = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    phone_number = models.IntegerField(blank=True)

    def image_url(self):
        if self.image:
            image_url = self.image.url
        else:
            image_url = '/static/img/default_profile_image.jpg'
        return image_url


    def __str__(self):
        return self.nickname
