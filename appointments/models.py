from django.db import models
from accounts.models import User
from django.conf import settings


class Appointment(models.Model):

    doctor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="doctor_appointments"
    )

    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="patient_appointments"
    )

    date = models.DateField()
    time = models.TimeField()

    status = models.CharField(
        max_length=20,
        default="pending"
    )

class Availability(models.Model):

    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    ) 

    date = models.DateField()

    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.doctor.username} - {self.date}"