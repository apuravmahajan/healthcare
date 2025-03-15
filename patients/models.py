from django.db import models

# Create your models here.
class Patient_Model (models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    age = models.DecimalField(max_digits=3, decimal_places=1)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    height = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.name