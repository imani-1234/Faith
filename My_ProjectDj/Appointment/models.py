from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50,
        choices=[
            ('uzazi', 'uzazi'),
            ('meno', 'meno'),
            ('kawaida', 'kawaida'),
            ('mifupa','mifupa'),
        ],
    )
    description = models.TextField() 
    image = models.ImageField(upload_to='location_images/', blank=True)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class patients(models.Model):
    reg = models.CharField(max_length=100)
    contact = models.IntegerField()
    allocated = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.patients.reg} for {self.Doctor.category}"

class appointment(models.Model):
    day = models.DateField()
    time = models.TimeField()
    customer = models.ForeignKey(Doctor, on_delete= models.CASCADE, null = True , blank = True)

    # def __str__(self):
    #     return f"Applied by {self.appointment.day} for {self.appointment.customer}"