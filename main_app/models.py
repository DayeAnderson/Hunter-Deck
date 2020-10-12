from django.db import models
from django.urls import reverse

# Create your models here.

class Weapon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    rarity = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('weapons_detail', kwargs={'pk': self.id})

class Hunter(models.Model):
    name = models.CharField(max_length=100)
    rank = models.IntegerField()
    gender = models.CharField(max_length=100)
    favorite_meal = models.CharField(max_length=100)
    weapons = models.ManyToManyField(Weapon)


    def __str__(self):
        return self.name
    
  # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'hunter_id': self.id})