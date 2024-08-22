from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializer import PrescriptionSerializer
from .models import Prescription

class PrescriptionAPI (APIView):

    def get(self, request):
        pre = Prescription.objects.all()
        serializer = PrescriptionSerializer(pre, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        data = request.data
        serializer = PrescriptionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res = {'detail': 'Data has been created Successfully'}
            return Response(res,status=status.HTTP_200_OK)

        return Response( serializer.errors, status=status.HTTP_200_OK)

    def delete(self, request):
        pre = request.data
        id = pre.get('id')
        pre = Prescription.objects.get(id=id)
        pre.delete()
        res = {'detail': 'Student deleted successfully'}
        return Response(res,status=status.HTTP_200_OK)
    
    def put(self, request):
        pre = request.data
        id = pre.get('id')
        pre = Prescription.objects.get(id=id)
        pre.update()
        res = {'detail': 'Student updated successfully'}
        return Response(res,status=status.HTTP_200_OK)



        

        

    