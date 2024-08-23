from .serializers import AppointmentSerializer ,PatientSerializer
from .models import Patient,Appointment
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


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
        res = {'detail': 'patent data deleted successfully'}
        return Response(res,status=status.HTTP_200_OK)
    
    def put(self, request):
        data = request.data
        id = data.get('id')
        data = Patient.objects.get(id=id)
        data.update()
        res = {'detail': 'data updated successfully'}
        return Response(res,status=status.HTTP_200_OK)

        # Get user profile
    def _get_profile(self, request):
        serializer = PatientSerializer(request.user, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Update profile details 
    def _update_profile(self, request):
        data = request.data
        if 'email' in  data :
            return Response({'detail': 'Not allowed to change email address'}, status=status.HTTP_400_BAD_REQUEST)
        
        if 'username' in data:
            return Response({'detail': 'Not allowed to change username'}, status=status.HTTP_400_BAD_REQUEST)
        
        try :
            serializer = PatientSerializer(request.user, data=data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e :
            return Response({'detail': f'Something went wrong', 'exception': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Manage user profile 
    @action(detail=False, methods=['get', 'patch'], permission_classes=[IsAuthenticated])
    def profile(self, request):
        if request.method == "get":
            return self._get_profile(request)
        else:
            return self._update_profile(request)



class AppointmentView(APIView):
    def get(self, request, *args, **kwargs):
        data = Appointment.objects.all()
        serializer = AppointmentSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request,name=None):

        data = request.data
        serializer = AppointmentSerializer(data=data)
        if serializer.is_valid():
            # serializer.save(doctor=request.user)
            serializer.save()
            res = {'detail': 'Data has been created Successfully'}
            return Response(res,status=status.HTTP_200_OK)

        return Response( serializer.errors, status=status.HTTP_200_OK)

    def delete(self, request):
        data = request.data
        id = data.get('id')
        data = Appointment.objects.get(id=id)
        data.delete()
        res = {'detail': 'data deleted successfully'}
        return Response(res,status=status.HTTP_200_OK)
    
