from django.db import models

from django.db import models


class Difficulty(models.Model):
    difficulty_id = models.AutoField(primary_key=True)
    difficulty = models.CharField(max_length=20)

    # for showing particular name in the drop down menu in admin panel
    def __str__(self):
        return self.difficulty


class Packages(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    total_days = models.CharField(max_length=20)
    start_price = models.IntegerField()
    img = models.ImageField(upload_to='Package_Images/')

    difficulty_id = models.ForeignKey(Difficulty, on_delete=models.CASCADE)

    # for showing particular name in the drop down menu in admin panel
    def __str__(self):
        return self.package_name


class Destination(models.Model):
    destination_id = models.AutoField(primary_key=True)
    destination = models.CharField(max_length=30)
    package_destination = models.ManyToManyField(Packages)

    # for showing particular name in the drop down menu in admin panel
    def __str__(self):
        return self.destination


class PackageDays(models.Model):
    days_id = models.AutoField(primary_key=True)
    days = models.CharField(max_length=10)

    # for showing particular name in the drop down menu in admin panel
    def __str__(self):
        return self.days


class PackagePlan(models.Model):
    package_id = models.ForeignKey(Packages, on_delete=models.CASCADE)
    days = models.ForeignKey(PackageDays, on_delete=models.CASCADE)
    plan_id = models.AutoField(primary_key=True)
    travel_details = models.CharField(max_length=40)
    difficulty_id = models.ForeignKey(Difficulty, on_delete=models.CASCADE)

    # for showing particular name in the drop down menu in admin panel
    def __str__(self):
        return self.travel_details


class Activities(models.Model):
    activities_id = models.AutoField(primary_key=True)
    activities = models.CharField(max_length=100)

    # for showing particular name in the drop down menu in admin panel
    def __str__(self):
        return self.activities


class TravelMode(models.Model):
    travel_id = models.AutoField(primary_key=True)
    travel_mode = models.CharField(max_length=20)

    # for showing particular name in the drop down menu in admin panel
    def __str__(self):
        return self.travel_mode


class ActivitiesTravelMode(models.Model):
    package_id = models.ForeignKey(Packages, on_delete=models.CASCADE)
    plan_id = models.ForeignKey(PackagePlan, on_delete=models.CASCADE)
    activities_id = models.ForeignKey(Activities, on_delete=models.CASCADE)
    travel_mode = models.ForeignKey(TravelMode, on_delete=models.CASCADE)


class PackageActivities(models.Model):
    package_id = models.ForeignKey(Packages, on_delete=models.CASCADE)
    plan_id = models.ForeignKey(PackagePlan, on_delete=models.CASCADE)
    activities_id = models.ForeignKey(Activities, on_delete=models.CASCADE)


class BookingRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    nationality = models.CharField(max_length=20)
    adults = models.IntegerField(max_length=20)
    children = models.IntegerField(max_length=20)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    airport_pickup = models.CharField(max_length=20)
    airline = models.CharField(max_length=20)
    flight_number = models.CharField(max_length=20)
    arrival_time = models.TimeField()
    package_Category = models.CharField(max_length=20)
    payment_mode = models.CharField(max_length=20)




