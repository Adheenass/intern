from rest_framework.routers import DefaultRouter
from django.urls import path, include
from prescription.views import PrescriptionAPI

urlpatterns = [
    path('prescription/', PrescriptionAPI.as_view()),
    
]
