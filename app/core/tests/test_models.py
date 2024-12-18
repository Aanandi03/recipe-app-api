"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
"""
get_user_model()  [Helper function for getting the User model]
-> returns the User model that is active in this project.
-> This is the same as doing from myapp.models import User
-> Allows referencing the User model by name, rather than by model class.
-> This is useful because the User model can be changed later on without affecting any code that references it by name.
-> This is a shortcut for:
    from myapp.models import User
    User = get_user_model()
-> Allows rederencing the User model without directly importing it.
-> Respects custom User models defined in settings.py.
"""


class ModelTests(TestCase):
    """Test models."""
    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))