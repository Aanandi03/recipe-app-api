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

**extra_fields: can provide keyword argumnets.
useful when u define additional fields
"""


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

# Manager associated to model.

class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'