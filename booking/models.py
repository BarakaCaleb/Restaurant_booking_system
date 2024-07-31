from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Table(models.Model):
    """creates model for all tables"""
    size = models.IntegerField(null=False, blank=False)
    category = models.CharField(max_length=10, null=False, blank=False)
    upper_limit = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return "Table " + str(self.pk) + " [" + self.category + "]"


class Timeslot(models.Model):
    """creates model for all timeslots"""
    time = models.TimeField(null=False, blank=False)

    def __str__(self):
        return str(self.time)


class Booking(models.Model):
    """creates model for all bookings"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking"
    )
    date = models.DateField(null=False, blank=False)
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="booking"
    )
    timeslot = models.ForeignKey(
        Timeslot, on_delete=models.CASCADE, related_name="booking"
    )

    def __str__(self):
        return (
            str(self.user) + " " + str(self.date) + " " + str(self.table) +
            " " + str(self.timeslot)
            )

    class Meta:
        ordering = ['date']
