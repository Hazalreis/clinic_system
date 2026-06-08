from rest_framework import serializers
from .models import Appointment, Availability

class AppointmentSerializer(serializers.ModelSerializer):

    def validate(self, data):
        
        doctor = data['doctor']
        date = data['date']
        time = data['time']

        availability = Availability.objects.filter(
            doctor = doctor,
            date = date,
        ).first()

        if not availability:
            raise serializers.ValidationError("Doctor not available")

        if not (availability.start_time <=  time <= availability.end_time):
            raise serializers.ValidationError(
            "Doctor is not available on this date."
        )

        if Appointment.objects.filter(
            doctor = doctor,
            date = date,
            time = time
        ).exists():
            raise serializers.ValidationError(
                "This time is already booked."
            )

        return data

    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ['patient', 'status']


class AvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Availability
        fields = '__all__'