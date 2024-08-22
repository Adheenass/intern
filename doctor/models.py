from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

class DoctorUser(AbstractUser):
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
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    specialization = models.CharField(max_length=100)
    available_days = models.CharField(max_length=3, choices=DAYS_CHOICES, null=True, blank=True)
    time_slot = models.TimeField()
    department = models.CharField(max_length=100 , null=True)


    groups = models.ManyToManyField(
        Group,
        related_name='doctoruser_set',  # Add a unique related_name
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='doctoruser_permissions_set',  # Add a unique related_name
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )




    def __str__(self):
        return self.username

class Prescription(models.Model):
    description = models.CharField(max_length=300)
    medicine = models.JSONField()
    test_date = models.DateField()

class EmailGeneration(models.Model):
    email = models.EmailField()  