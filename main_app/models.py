from django.db import models
from django.urls import reverse

# Create your models here.

class Hunter(models.Model):
    name = models.CharField(max_length=100)
    rank = models.IntegerField()
    gender = models.CharField(max_length=100)
    favorite_meal = models.CharField(max_length=100)

def __str__(self):
    return self.name
    
  # Add this method
def get_absolute_url(self):
    return reverse('detail', kwargs={'cat_id': self.id})