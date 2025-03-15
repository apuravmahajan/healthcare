from rest_framework import serializers
from .models import Patient_Model


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient_Model
        fields = ['id', 'name', 'birth_date', 'age', 'gender', 'height', 'weight']
