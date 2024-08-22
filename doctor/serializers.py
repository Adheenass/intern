from .models import DoctorUser, Prescription
from rest_framework import serializers

class DotorSerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorUser
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'