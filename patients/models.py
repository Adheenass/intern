from django.db import models
from doctor.models import DoctorUser
from django.contrib.auth.models import User


# Create your models here.
class Patient(models.Model):
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    weight = models.IntegerField()
    height = models.IntegerField()



class Appointment(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE ,null=True, related_name='appointments_as_doctor')
    patient = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='appointments_as_patient')
    appointment_time = models.TimeField()  # TimeField for storing time
    appointment_date = models.DateField()  # Optional DateField for storing the date
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Appointment with Dr. {self.doctor} at {self.appointment_time} on {self.appointment_date}"