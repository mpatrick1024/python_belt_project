from __future__ import unicode_literals
from django.db import models
from apps.login_dashboard_app.models import *

# Create your models here.

class JobManager (models.Manager):
    def job_validator (self, postData):
        errors = {}
        if len(postData['title']) == 0:
            errors['title_blank'] = 'Please enter job title.'
        elif len(postData['title']) < 2:
            errors['title_short'] = 'Title should be at least 2 characters.'

        if len(postData['description']) == 0:
            errors['description_blank'] = 'Please enter job description.'
        elif len(postData['description']) < 2:
            errors['description_short'] = 'Description should be at least 2 characters.'

        if len(postData['location']) == 0:
            errors['location_blank'] = 'Please enter job location.'
        elif len(postData['location']) < 2:
            errors['location_short'] = 'Location should be at least 2 characters.'
        return errors

class Job (models.Model):
    title = models.CharField (max_length=255)
    description = models.TextField ()
    location = models.CharField (max_length=255)
    category = models.CharField (max_length=255, null=True)
    other = models.CharField (max_length=255, null=True)
    user = models.ForeignKey (User, related_name="jobs", null=True)
    worker = models.ForeignKey (User, related_name="assignments", null=True)
    created_at = models.DateField (auto_now_add=True)
    objects = JobManager()
    def __repr__ (self):
        return f"<Job Object: {self.title}, ({self.id})>"