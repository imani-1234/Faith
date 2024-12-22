from django.contrib import admin
from .models import Doctor , patients , appointment
# Register your models here.
admin.site.register(Doctor)
admin.site.register(patients)
admin.site.register(appointment)