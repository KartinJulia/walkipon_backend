from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from django.conf import settings

class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not password:
            raise ValueError('User must have a password')
        user = self.model(username = username, email = self.normalize_email(email), password = password)
        user.is_admin = False
        user.is_active = True
        user.save(using = self._db)
        return user

    def create_superuser(self, username, email, password):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not password:
            raise ValueError('Users must have a password')
        user = self.model(username = username, email = self.normalize_email(email), password = password)
        user.is_admin = True
        user.is_active = True
        user.save(using = self._db)
        return user
