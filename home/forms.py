from django import forms


class BookingForm(forms.Form):

    name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=20)
    address = forms.CharField(max_length=50)
    nationality = forms.CharField(max_length=20)
    adults = forms.IntegerField()
    children = forms.IntegerField()
    arrival_date = forms.DateField()
    departure_date = forms.DateField()
    airport_pickup = forms.CharField(max_length=20)
    airline = forms.CharField(max_length=20)
    flight_number = forms.CharField(max_length=20)
    arrival_time = forms.TimeField()
    package_Category = forms.CharField(max_length=20)
    payment_mode = forms.CharField(max_length=20)