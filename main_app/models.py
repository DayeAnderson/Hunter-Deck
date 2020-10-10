from django.db import models

# Create your models here.

class Hunter(models.Model):
    name = models.CharField(max_length=100)
    rank = models.IntegerField()
    gender = models.CharField(max_length=100)
    favorite_meal = models.CharField(max_length=100)