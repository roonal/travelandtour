from django.urls import path
from . import views
from django.urls import include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.register, name='register'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('package-booking/', views.package_booking, name="booking_form"),
    path('booking-request/', views.booking_request, name="booking-request"),


    # path('password_change/done/',
    #      auth_views.PasswordChangeDoneView.as_view(template_name='user-auth/password_change_done.html'),
    #      name='password_change_complete'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(template_name='user-auth/password_change.html'),
    #      name='password_change'),
    # path('password_reset/done/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name='user-auth/password_reset_done.html'),
    #      name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('reset/done/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name='user-auth/password_reset_complete.html'),
    #      name='password_reset_complete'),

]