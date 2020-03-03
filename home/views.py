from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Packages, Destination, Difficulty, PackageActivities,PackagePlan,PackageDays,TravelMode,ActivitiesTravelMode


def index(request):
    context = {'packages': Packages.objects.all()}
    return render(request, 'user/index.html', context)


def package_details(request, pk):
    context = {'packages': Packages.objects.filter(package_id=pk),
               'difficulty': Difficulty.objects.filter(difficulty_id=pk),
               'destination': Destination.objects.filter(package_destination=pk),
               'package_plan': PackagePlan.objects.filter(package_id=pk),
               'day': PackagePlan.objects.filter(package_id=pk),
               'activities': PackageActivities.objects.filter(package_id=pk),
               'travel_mode': ActivitiesTravelMode.objects.filter(package_id=pk)

               }
    return render(request, 'user/package_details.html', context)


def package_booking(request):
    return render(request, 'user/booking_form.html')



