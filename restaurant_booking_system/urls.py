"""restaurant_booking_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from booking.views import home_page
from booking.views import view_index
from booking.views import open_contacts
from booking.views import make_booking
from booking.views import edit_booking
from booking.views import delete_booking
# from booking.views import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='Home'),
    path('index/', view_index, name='Index'),
    path('contacts/', open_contacts, name='Contacts'),
    path('booking/', make_booking, name='Make Booking'),
    path('edit/<booking_id>', edit_booking, name='Edit Booking'),
    path('delete/<booking_id>', delete_booking, name='Delete Booking'),
    path('accounts/', include('allauth.urls')),
]
