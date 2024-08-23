from .models import DoctorUser, Prescription
from rest_framework import serializers

class DotorSerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorUser
        fields = ['gender','available_days','starting_time','department','end_time','d_user']

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'