from django.db import models
from django.contrib.postgres.fields import ArrayField

class House(models.Model):
  name = models.CharField(max_length=1000)
  description = models.CharField(max_length=5000)
  city = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  longitude = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
  latitude = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  amenities = ArrayField(models.CharField(max_length=20, null=True, blank=True), default=list, null=True, blank=True)
  featured = models.BooleanField(default=False, null=True, blank=True)
  guests = models.IntegerField(null=True, blank=True)
  bedrooms = models.IntegerField(null=True, blank=True)
  baths = models.IntegerField(null=True, blank=True)
  beds = models.IntegerField(null=True, blank=True)

  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
