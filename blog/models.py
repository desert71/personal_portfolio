from django.db import models
from django import forms

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    text = models.CharField(max_length=50000)

