from django.db import models
from .user import User
from .house import House

class Booking(models.Model):
  start = models.DateField()
  end = models.DateField()
  guest = models.ForeignKey(User, on_delete=models.CASCADE)
  property = models.ForeignKey(House, related_name='bookings', on_delete=models.CASCADE)

  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

  def __str__(self):
    return f'Booking for guest no. {self.guest} at {self.property}'
