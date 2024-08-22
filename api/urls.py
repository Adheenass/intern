from django.urls import path, include
from doctor.views import PrescriptionAPI
from doctor.views import DoctorView
from patients.views import PatientView,AppointmentView

urlpatterns = [
    path('prescription/', PrescriptionAPI.as_view()),
    path('doctor/', DoctorView.as_view()),
    path('patient/', PatientView.as_view()),

    
]
