from .models import Doctor_Model
from rest_framework import serializers

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor_Model
        fields = ['id', 'name', 'specialization']