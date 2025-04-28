"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

"""
AbstractBaseUser: (Functionality for auth system)
    - This is a base class that provides the core functionality of a user in Django.
    - It defines the basic fields and methods that a user should have, such as email, password, and permissions.
    - It also provides a way to authenticate users and check their permissions.

BaseUserManager: Base class for managing users with some helper methods such as
    normalize_email

PermissionsMixin: Support for django permission system
                  Includes fields and methods

**extra_fields: can provide keyword argumnets.
useful when u define additional fields (gives the flexibility to create different field in a user - dynamic)
"""


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)


        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

# Manager associated to model.  self.model = User....User Object

class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager() # Creates instance of the manager

    USERNAME_FIELD = 'email'

    """ Defines the field that we want to use for authentication (with this we can set our custom default field for user)"""