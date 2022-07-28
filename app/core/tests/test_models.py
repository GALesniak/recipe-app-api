"""
Tests for models
"""
from decimal import Decimal

from webbrowser import get
from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

class ModelTests(TestCase):
    """ Test Models """

    def test_create_user_with_email_successful(self):
        """ Test user with email creation """
        email = 'johndoe@example.com'
        password = '123john'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test email is normalized for new users """
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_has_email(self):
        """ In case no email provided raises ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('','test111')

    def test_create_superuser(self):
        """ Test creating a SuperUser """
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test1243',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """ Test creating a recipe is successful """
        user = get_user_model().objects.create_user(
            'test@example.com',
            'test1243',
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample food name',
            time_minutes=5,
            price=Decimal('5.55'),
            description='Sample tasty food',
        )

        self.assertEqual(str(recipe), recipe.title)
