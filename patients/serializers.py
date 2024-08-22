from .models import Appointment
from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'appointment_date', 'appointment_time']
        

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'mobile_number']