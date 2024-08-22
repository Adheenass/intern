from django.shortcuts import render
from .serializers import DotorSerializer, PrescriptionSerializer
from .models import DoctorUser, Prescription,EmailGeneration
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
# emailneed
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings


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

      # Get user profile
    def _get_profile(self, request):
        serializer = DotorSerializer(request.user, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Update profile details 
    def _update_profile(self, request):
        data = request.data
        if 'email' in  data :
            return Response({'detail': 'Not allowed to change email address'}, status=status.HTTP_400_BAD_REQUEST)
        
        if 'username' in data:
            return Response({'detail': 'Not allowed to change username'}, status=status.HTTP_400_BAD_REQUEST)
        
        try :
            serializer = DotorSerializer(request.user, data=data, partial=True, context={'request': request})
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




#### email_generation 



def subscribe(request):
    form = EmailGeneration()
    if request.method == 'POST':
        form = EmailGeneration(request.POST)
        if form.is_valid():
            subject = 'Remainding the test Date'
            message = 'Sending Email through Gmail'
            recipient = form.cleaned_data.get('email')
            send_mail(subject, 
              message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('subscribe')
    return render(request, 'subscriptions/home.html', {'form': form})