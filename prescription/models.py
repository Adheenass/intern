from django.db import models

# Create your models here.

class Prescription(models.Model):
    description = models.CharField(max_length=300)
    medicine = models.JSONField()
    test_date = models.DateField()
