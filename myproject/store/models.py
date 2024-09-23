from django.db import models

# Create your models here.
class About(models.Model):
    discription = models.CharField(max_length=500)
    title= models.CharField(max_length=100)
    icon= models.CharField(max_length=100, default='empty')

