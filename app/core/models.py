from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fieds):
        """Create and saves new user"""
        if not email:
            raise ValueError("e-mail required")
        user = self.model(email=self.normalize_email(email), **extra_fieds)
        user.set_password(password)
        user.save(self._db)

        return user

    def create_superuser(self, email, password):
        """Create and saves new superuser"""
        user = self.create_user(email, password)
        user.is_superuser = user.is_staff = True
        user.save(self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports mail instead of name"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserManager()
    USERNAME_FIELD = 'email'
