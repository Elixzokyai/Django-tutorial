from enum import unique

from django.db import models
from django.utils.formats import date_format


# Create your models here.
# this step should create a table task in our db where the attributes will be the column
class Task(models.Model):
    #attributes
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    Author = models.CharField(max_length=100)
    published = models.DateField()


    def __str__(self):
        return self.title

