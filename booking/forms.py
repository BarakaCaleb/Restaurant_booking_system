from django import forms
from .models import Booking
from django.contrib.auth.models import User


class BookingForm(forms.ModelForm):
    """creates form for user to user when booking or updating a booking"""
    class Meta:
        model = Booking
        fields = ['date', 'table', 'timeslot']
