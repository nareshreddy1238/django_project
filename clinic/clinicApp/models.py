from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

class ClinicalData(models.Model):
    COMPENENT_NAMES = [ ('hw','Height/Weoght'),('bp', 'Blood Pressure'),('heartrate', 'Heart Rate')]
    component_name = models.CharField(choices=COMPENENT_NAMES, max_length=30)
    component_value = models.CharField(max_length=30)
    measured_date_time = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
