from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

from jdlib.django.fields import AutoCreatedField, AutoLastModifiedField, UUIDField


class TimeStampedMixin(models.Model):
    created_at = AutoCreatedField()
    updated_at = AutoLastModifiedField()

    def save(self, *args, **kwargs):
        update_fields = kwargs.get('update_fields', None)
        if update_fields is not None:
            kwargs['update_fields'] = set(update_fields).union('updated_at')
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    uuid = UUIDField(_('UUID'))

    class Meta:
        abstract = True


class Model(TimeStampedMixin, UUIDMixin):
    class Meta:
        abstract = True


class User(AbstractUser, UUIDMixin):
    class Meta:
        abstract = True


class EmailUserManager(UserManager):
    def _create_user(self, email: str, username: str | None, password: str | None, **extra_fields):
        '''
        Create and save user with the given email, username, and password.
        '''
        if not email:
            raise ValueError('The given email must be set.')
        email = self.normalize_email(email)
        if username is not None:
            # Load model from app registry versus get_user_model
            # so this manager method can be used in migrations
            GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
            username = GlobalUserModel.normalize_username(username)
        user = self.model(email=email, username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
        
    def create_user(self, email: str, username: str | None=None, password: str | None=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)

    def crete_superuser(self, email: str, username: str | None=None, password: str | None=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self._create_user(email, username, password, **extra_fields)


class EmailUser(User):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True, blank=True)

    objects = EmailUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        abstract = True

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if self.username is None:
            self.username = self.uuid.hex
        super().save(*args, **kwargs)
