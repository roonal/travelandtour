from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('<pk>/', views.package_details, name="package_details"),
    path('<pk>/', views.package_details_final, name="package_details"),

]