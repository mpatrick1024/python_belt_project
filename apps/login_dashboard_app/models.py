from __future__ import unicode_literals
from django.db import models


import re

# Create your models here.
EMAIL_REGIX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager (models.Manager):
    def user_validator (self, postData):
        errors = {}
        email_taken = User.objects.filter (email = postData['email'])
        if len(postData['email']) == 0:
            errors['email_blank'] = 'Please enter your email.'
        elif not EMAIL_REGIX.match (postData['email']):
            errors['email_invalid'] = 'Please enter a valid email address.'
        elif len(email_taken) > 0:
            errors['email_used'] = 'That email is already in use.'

        if len(postData['first_name']) == 0:
            errors['first_name_blank'] = 'Please enter your first name.'
        elif len(postData['first_name']) < 2:
            errors['first_name_short'] = 'First name should be at least 2 characters.'

        if len(postData['last_name']) == 0:
            errors['last_name_blank'] = 'Please enter your last name.'
        elif len(postData['last_name']) < 2:
            errors['last_name_short'] = 'Last name should be at least 2 characters.'

        if len(postData['password']) == 0:
            errors['password_blank'] = 'Please enter your password.'
        elif len(postData['password']) < 8:
            errors['password_short'] = 'Password must have at least 8 characters.'

        if (postData['password'] != postData['confirm_pw']):
            errors['password_match_fail'] = 'Passwords do not match.'
        return errors
        
    def login_validator (self, postData):
        errors = {}
        user = User.objects.filter (email = postData['email'])
        if len(postData['email']) == 0:
            print ('Did not find email in database')
            errors['invalid'] = 'Invalid login credentials'
        else:
            user = User.objects.get (email = postData['email'])
            if postData['password'] == user.password:
                print('Valid password, Login Success')
            else:
                print("Invalid password, Login Unsuccessful")
                errors['invalid'] = "Invalid login credentials."
        return errors

class User (models.Model):
    first_name = models.CharField (max_length=255)
    last_name = models.CharField (max_length=255)
    email = models.CharField (max_length=255)
    password = models.CharField (max_length=255)
    objects = UserManager()
    def __repr__ (self):
        return f"<Show Object: {self.first_name} {self.last_name}, ({self.id})>"

