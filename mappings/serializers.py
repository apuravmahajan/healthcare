from rest_framework import serializers
from .models import Mappings_Model
from patients.models import Patient_Model
from doctors.models import Doctor_Model

class MappingSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient_Model.objects.all())
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor_Model.objects.all(), many=True)

    class Meta:
        model = Mappings_Model
        fields = '__all__'