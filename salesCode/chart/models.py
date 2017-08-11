from django.db import models

# Create your models here.
class Category(models.Model):
    area = models.CharField(max_length = 255)
    category = models.CharField(max_length = 255)
    lat = models.FloatField()
    lan = models.FloatField()
    price = models.IntegerField()

objects = models.Manager() #For avoiding pylint error of no objects for category
