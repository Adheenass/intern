from django.shortcuts import render
from .serializers import AppointmentSerializer ,PatientSerializer
from .models import Patient,Appointment
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class PatientView(APIView):

    def get(self, request):
        data = Patient.objects.all()
        serializer = PatientSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        data = request.data
        serializer = PatientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res = {'detail': 'Data has been created Successfully'}
            return Response(res,status=status.HTTP_200_OK)

        return Response( serializer.errors, status=status.HTTP_200_OK)

    def delete(self, request):
        data = request.data
        id = data.get('id')
        data = Patient.objects.get(id=id)
        data.delete()
        res = {'detail': 'Student deleted successfully'}
        return Response(res,status=status.HTTP_200_OK)
    
    def put(self, request):
        data = request.data
        id = data.get('id')
        data = Patient.objects.get(id=id)
        data.update()
        res = {'detail': 'Student updated successfully'}
        return Response(res,status=status.HTTP_200_OK)

class AppointmentView(APIView):
    def get(self, request):
        data = Appointment.objects.all()
        serializer = AppointmentSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        data = request.data
        serializer = AppointmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res = {'detail': 'Data has been created Successfully'}
            return Response(res,status=status.HTTP_200_OK)

        return Response( serializer.errors, status=status.HTTP_200_OK)

    def delete(self, request):
        data = request.data
        id = data.get('id')
        data = Appointment.objects.get(id=id)
        data.delete()
        res = {'detail': 'Student deleted successfully'}
        return Response(res,status=status.HTTP_200_OK)
    