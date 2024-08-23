from django.db import models
from django.contrib.auth.models import User

class DoctorUser(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    DAYS_CHOICES = [
        ('Mon','monday'),
        ('Tue','tuesday'),
        ('Wed','wednesday'),
        ('Thu','thursday'),
        ('Fri','friday'),
        ('Sat','saturday'),
        ('Sun','sunday'),

    ]
    
    d_user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    specialization = models.CharField(max_length=100)
    available_days = models.CharField(max_length=3, choices=DAYS_CHOICES, null=True, blank=True)
    starting_time = models.TimeField(null=True)
    end_time =models.TimeField(null=True)
    department = models.CharField(max_length=100 , null=True)

    def __str__(self):
        return self.username

class Prescription(models.Model):
    description = models.CharField(max_length=300)
    medicine = models.JSONField()
    test_date = models.DateField()

class EmailGeneration(models.Model):
    email = models.EmailField()  