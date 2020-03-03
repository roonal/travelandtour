from django.db import models
from django.forms import ModelForm
# Create your models here.


class BookingRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    nationality = models.CharField(max_length=20)
    adults = models.IntegerField()
    children = models.IntegerField()
    arrival_date = models.DateField()
    departure_date = models.DateField()
    airport_pickup = models.CharField(max_length=20)
    airline = models.CharField(max_length=20)
    flight_number = models.CharField(max_length=20)
    arrival_time = models.TimeField()
    package_Category = models.CharField(max_length=20)
    payment_mode = models.CharField(max_length=20)


class Booking(ModelForm):
    class Meta:
        model = BookingRequest
        exclude = ('request_id',)
