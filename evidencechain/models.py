from tkinter import CASCADE
from django.db import models
from datetime import datetime

# Create your models here.


class Case(models.Model):
    caseNumber = models.CharField(max_length=100, null=False)
    creator = models.CharField(max_length=100, null=True)
    starting_date = models.DateTimeField(auto_now_add=True, blank=True)


class Evidence(models.Model):
        caseNumber = models.CharField(max_length=100, null=True)
        creator = models.CharField(max_length=100, null=True)
        date = models.DateTimeField(auto_now_add=True, null=True)
        description = models.CharField(max_length=10000)


