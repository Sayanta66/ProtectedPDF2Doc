from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.CharField(max_length=255)

class photos(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')