from django.shortcuts import render
from .serializers import DotorSerializer
from .models import DoctorUser
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class DoctorView(APIView):

    def get(self, request):
        data = DoctorUser.objects.all()
        serializer = DotorSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        data = request.data
        serializer = DotorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res = {'detail': 'Data has been created Successfully'}
            return Response(res,status=status.HTTP_200_OK)

        return Response( serializer.errors, status=status.HTTP_200_OK)

    def delete(self, request):
        data = request.data
        id = data.get('id')
        data = DoctorUser.objects.get(id=id)
        data.delete()
        res = {'detail': 'Student deleted successfully'}
        return Response(res,status=status.HTTP_200_OK)
    
    def put(self, request):
        data = request.data
        id = data.get('id')
        data = DoctorUser.objects.get(id=id)
        data.update()
        res = {'detail': 'Student updated successfully'}
        return Response(res,status=status.HTTP_200_OK)