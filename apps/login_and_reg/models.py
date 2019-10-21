from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least two characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least two characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"
        elif len(User.objects.filter(email=postData['email'])) > 0:
            errors['email'] = "This email address already exists"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        elif postData['password'] != postData['conf_password']:
            errors['password'] = "Passwords do not match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()




# Create your models here.
