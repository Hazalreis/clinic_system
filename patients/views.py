from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer


@api_view(['GET'])
def get_patients(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_patient(request):

    serializer = PatientSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            "message": "Patient Added Successfully"
        })
    
    return Response(serializer.errors)

@api_view(['PUT'])
def update_patient(request, id):

    patient = get_object_or_404(Patient, id=id)

    serializer = PatientSerializer(patient, data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            "message" : "patient updated successfully"
        })
    
    return Response(serializer.errors)


@api_view(['DELETE'])
def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)

    patient.delete()

    return Response({
        "message" : "patient deleted succesfully"
    })