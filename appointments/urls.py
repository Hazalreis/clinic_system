from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create_appointment),
    path('doctor/', doctor_appointments),
    path('patient/', patient_dashboard),
    path('confirm/<int:id>/', confirm_appointment),
]