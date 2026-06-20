from django.urls import path
from .views import *

urlpatterns = [
    path('create_appointment/', create_appointment),
    path('doctor/', doctor_appointments),
    path('patient/', patient_dashboard),
    path('availability/', availability),
    path('get_availability/', get_availability),
    path('confirm/<int:id>/', confirm_appointment),
    path('me/', me)
]