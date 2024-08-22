from .models import DoctorUser
from rest_framework import serializers

class DotorSerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorUser
        fields = '__all__'