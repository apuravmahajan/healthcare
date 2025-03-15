from django.db import models

# Create your models here.
class Mappings_Model(models.Model):
    patient = models.ForeignKey('patients.Patient_Model', on_delete=models.CASCADE)
    doctor = models.ManyToManyField('doctors.Doctor_Model')