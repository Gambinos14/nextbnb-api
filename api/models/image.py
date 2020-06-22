from django.db import models
from .house import House

class Image(models.Model):
  url = models.CharField(max_length=3000)
  house_id = models.ForeignKey(House, related_name='images', on_delete=models.CASCADE)
