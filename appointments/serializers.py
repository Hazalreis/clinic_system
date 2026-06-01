from rest_framework import serializers
from .models import Appointment, Availability

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'


class AvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Availability
        fields = '__all__'