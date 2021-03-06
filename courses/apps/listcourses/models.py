from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Course name should be more than 5 characters"
        if len(postData['description']) < 10:
            errors["description"] = "Course descripton should be more than 10 characters"
        return errors;
class course(models.Model):
      name = models.CharField(max_length=255)
      description = models.TextField()
      coursenumber=models.IntegerField()
      semester=models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      objects = CourseManager()