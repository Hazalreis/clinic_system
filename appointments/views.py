from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Appointment, Availability
from rest_framework import status
from .serializers import AppointmentSerializer, AvailabilitySerializer
from rest_framework.permissions import BasePermission



class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == "doctor"
        )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_appointment(request):

    serializer = AppointmentSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save(
            patient = request.user,
            status="pending"
        )

        return Response(
            {"message" : "Appointment created"},
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )



@api_view(['POST'])
@permission_classes([IsDoctor])
def availability(request):

    serializer = AvailabilitySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(
            doctor = request.user
        )
        return Response(
            {"message" : "Availability created"},
            status=status.HTTP_201_CREATED
            )
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_availability(request):

    doctor_id = request.GET.get('doctor_id')

    queryset = Availability.objects.all()

    if doctor_id:
        queryset = queryset.filter(doctor_id=doctor_id)

    serializer = AvailabilitySerializer(queryset, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def doctor_appointments(request):

    appointments = Appointment.objects.filter(
        doctor = request.user
    )

    serializer = AppointmentSerializer(appointments, many=True)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def confirm_appointment(request,id):

    appointment = Appointment.objects.get(id=id)

    if request.user.role != 'doctor':
        return Response({"error": "Only doctors allowed"}, status=403)
    
    if appointment.doctor != request.user:
        return Response({"error": "Not your appointment"}, status=403)
    
    appointment.status = "confirmed"
    appointment.save()

    return Response({"message": "Appointment confirmed"})