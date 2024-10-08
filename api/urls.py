from django.urls import path, include
from doctor.views import PrescriptionAPI
from doctor.views import DoctorView, SendEmailView
from patients.views import PatientView,AppointmentView
from accounts.views import AccountsViewSet


urlpatterns = [

    # ------------------ACCOUNT------------------------
    path('register/', AccountsViewSet.as_view({'post': 'register'})),
    path('login/', AccountsViewSet.as_view({'post': 'login'})),
    path('logout/',AccountsViewSet.as_view({'post': 'logout'})),
    path('delete/',AccountsViewSet.as_view({'post': 'delete'})),


    # ------------------DOCTOR------------------------
    path('doctor/profile/', DoctorView.as_view()),
    path('doctor/prescription/<str:name>', PrescriptionAPI.as_view()),
    path('doctor/prescription/email/<str:email>', SendEmailView.as_view()),
    # path('doctor/get_patient/', PatientView.as_view({'put':'_get_profile'})),




    # ------------------PATIENT------------------------

    path('patient/profile/', PatientView.as_view()),
    path('patient/prescription/', PrescriptionAPI.as_view()),
    path('patient/appointment/<str:name>', AppointmentView.as_view()),

    
]
