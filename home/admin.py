from django.contrib import admin
from .models import Packages, Difficulty, Destination,PackageDays,PackagePlan,Activities,PackageActivities
from .models import TravelMode,ActivitiesTravelMode

admin.site.register(Difficulty)
admin.site.register(Packages)
admin.site.register(Destination)
admin.site.register(PackageDays)
admin.site.register(PackagePlan)
admin.site.register(Activities)
admin.site.register(PackageActivities)
admin.site.register(TravelMode)
admin.site.register(ActivitiesTravelMode)







