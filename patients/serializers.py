from .models import Appointment
from rest_framework import serializers
from .models import Patient

class AppointmentSerializer(serializers.Serializer):
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'appointment_date', 'appointment_time']
        

class PatientSerializer(serializers.Serializer):
    class Meta:
        model = Patient
        fields = '__all__'