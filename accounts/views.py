from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate

from django.contrib.auth.models import User
from .serializers import RegisterSerializer,LoginSerializer

# Create your views here.
class AccountsViewSet(ViewSet):

    # Register new user with username, email and password. 
    @action(detail=False, methods=['post'])
    def register(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                data = serializer.validated_data
                user = User.objects.create_user(password=data['password'], email=data['email'])
                token, created = Token.objects.get_or_create(user=user)
                return Response({'data': RegisterSerializer(user).data, 'token': token.key }, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e :
            return Response({'detail': f'Something went wrong', 'exception': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
     # Login user with email and password
    @action(detail=False, methods=['post'])
    def login(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data['email']
                password = serializer.validated_data['password']
                user = authenticate(email=email, password=password)
                if user is not None:
                    token, created = Token.objects.get_or_create(user=user)
                    return Response({'token':token.key, 'username': user.username, 'email': user.email}, status=status.HTTP_200_OK)
                else :
                    return Response({'detail': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            else :
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e :
            return Response({'detail': f'Something went wrong', 'exception': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # Logout
    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])    
    def logout(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'detail':'Successfully logged out'}, status=status.HTTP_200_OK)
        except Exception as e :
            return Response({'detail': f'Something went wrong', 'exception': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # Delete account
    @action(detail=False, methods=['delete'], permission_classes=[IsAuthenticated]) 
    def delete(self, request):
        try :
            request.user.delete()
            return Response({'detail': 'User deleted successfully'}, status=status.HTTP_200_OK)

        except Exception as e :
            return Response({'detail': f'Something went wrong', 'exception': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    