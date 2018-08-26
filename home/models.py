from django.db import models

# Create your models here.
class Items(models.Model):
    head = models.CharField(max_length=255, default='DEFAULT VALUE')
    info = models.CharField(max_length=255)
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
