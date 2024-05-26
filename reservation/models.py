from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    number_of_guests = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.name} - {self.booking_date} at {self.booking_time}"
