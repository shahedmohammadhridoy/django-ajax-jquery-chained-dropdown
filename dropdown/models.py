from unittest.util import _MAX_LENGTH
from django.db import models

class Programming(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name

class Course(models.Model):
    programming = models.ForeignKey(Programming, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name
