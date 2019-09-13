from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

from validators import validateChar

import uuid


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_admin=False, firstName=None, lastName=None):
        if not email:
            raise ValueError('User must have an email address')
        if not password:
            raise ValueError('User must have a password')

        user_obj = self.model(email=self.normalize_email(email))
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.firstName = firstName
        user_obj.lastName = lastName
        user_obj.uid = uuid.uuid4()
        user_obj.set_password(password)
        user_obj.last_login=now()
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_admin=True,
            firstName='',
            lastName=''
        )
        return user


class Accounts(AbstractBaseUser):
    email = models.EmailField(max_length=64, unique=True)
    firstName = models.CharField(max_length=16, blank=True, validators=[validateChar])          # first name
    lastName = models.CharField(max_length=16, blank=True, validators=[validateChar])           # last name
    active = models.BooleanField(default=True)                                                  # can login
    admin = models.BooleanField(default=False)                                                  # superuser
    dateJoined = models.DateTimeField(default=now, editable=False)
    uid = models.CharField(max_length=64, editable=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Accounts'

    @property
    def get_short_name(self):
        return self.firstName

    @property
    def get_full_name(self):
        return self.firstName + ' ' + self.lastName

    @property
    def is_staff(self):
        return self.admin

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    def has_perm(self, perm, obj=None):
        return self.active

    def has_perms(self, perm, obj=None):
        return self.active

    def has_module_perms(self, app_label):
        return self.active