from django.test import TestCase
from .models import Booking

class BookingModelTest(TestCase):
    def setUp(self):
        Booking.objects.create(name="Test", email="test@example.com", phone_number="1234567890", booking_date="2023-01-01", booking_time="12:00:00", number_of_guests=4)

    def test_booking_creation(self):
        booking = Booking.objects.get(name="Test")
        self.assertEqual(booking.email, "test@example.com")
