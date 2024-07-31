from django.contrib import admin
from .models import Table
from .models import Timeslot
from .models import Booking

# Register your models here.
admin.site.register(Table)
admin.site.register(Timeslot)
admin.site.register(Booking)
