from django.urls import path
from .views import *

urlpatterns = [
    path('patients/', get_patients),
    path('patients/add/', add_patient),
    path('patients/<int:id>/', update_patient),
    path('patients/delete/<int:id>/', delete_patient),
]