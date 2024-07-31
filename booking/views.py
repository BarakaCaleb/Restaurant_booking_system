from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .models import Table
from .models import Timeslot
from django.contrib.auth.models import User
from .forms import BookingForm

# Create your views here.


def home_page(request):
    """redirects user to home page"""
    return render(request, 'booking/home.html')


def view_index(request):
    """redirects user to index page"""
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'booking/index.html', context)


def open_contacts(request):
    """redirects user to contacts page"""
    return render(request, 'booking/contacts.html')


def make_booking(request):
    """redirects user to bookings page"""
    is_new = True
    if request.method == 'POST':
        """updates bookings database if booking is valid"""
        form = BookingForm(request.POST)
        if form.is_valid():
            user = request.user
            date = form.cleaned_data['date']
            table = form.cleaned_data['table']
            timeslot = form.cleaned_data['timeslot']
            is_new = validate_booking(date, table, timeslot)
            if is_new:
                Booking.objects.create(
                    user=user, date=date,
                    table=table,
                    timeslot=timeslot
                    )
                return redirect('Index')
            else:
                form = BookingForm()
                context = {
                    'form': form,
                    'is_new': is_new
                }
                return render(request, 'booking/booking.html', context)
    form = BookingForm()
    context = {
        'form': form,
        'is_new': is_new
    }
    return render(request, 'booking/booking.html', context)


def validate_booking(date, table, timeslot):
    """validates the booking"""
    check_booking = Booking.objects.filter(
        date=date, table=table,
        timeslot=timeslot
        )
    if check_booking.__len__() > 0:
        return False
    else:
        return True


def edit_booking(request, booking_id):
    """redirects user to the edit page"""
    booking = get_object_or_404(Booking, id=booking_id)
    is_new = True
    if request.method == 'POST':
        """updates bookings database if booking is valid"""
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            user = request.user
            date = form.cleaned_data['date']
            table = form.cleaned_data['table']
            timeslot = form.cleaned_data['timeslot']
            is_new = validate_booking(date, table, timeslot)
            if is_new:
                booking.delete()
                Booking.objects.create(
                    user=user, date=date,
                    table=table,
                    timeslot=timeslot
                    )
                return redirect('Index')
            else:
                form = BookingForm(instance=booking)
                context = {
                    'form': form,
                    'is_new': is_new
                }
                return render(request, 'booking/edit_booking.html', context)
    form = BookingForm(instance=booking)
    context = {
        'form': form,
        'is_new': is_new
    }
    return render(request, 'booking/edit_booking.html', context)


def delete_booking(request, booking_id):
    """deletes selected booking from the database"""
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('Index')
