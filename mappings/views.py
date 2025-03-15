from rest_framework.views import APIView
from .serializers import MappingSerializer
from .models import Mappings_Model
from rest_framework.response import Response
from patients.models import Patient_Model
from doctors.models import Doctor_Model
from rest_framework.permissions import IsAuthenticated

class Mapping_View(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id=None):
        if id is None:
            mappings = Mappings_Model.objects.all()
            serializer = MappingSerializer(mappings, many=True)
            return Response(serializer.data, status=200)
        else:
            try:
                patient = Patient_Model.objects.get(id=id)
                mapping = Mappings_Model.objects.get(patient=patient)
                serializer = MappingSerializer(mapping)
                return Response(serializer.data, status=200)
            except Mappings_Model.DoesNotExist:
                return Response({"error": "Mapping not found"}, status=404)
            
    def post(self, request):
        patient_id = request.data.get('patient') 
        doctor_ids = request.data.get('doctor', [])
        patient = Patient_Model.objects.get(id=patient_id)
        try:
            mapping, created = Mappings_Model.objects.get_or_create(patient=patient)

            if created:
                doctors = Doctor_Model.objects.filter(id__in=doctor_ids)
                mapping.doctor.set(doctors)
            else:
                doctors = Doctor_Model.objects.filter(id__in=doctor_ids)
                mapping.doctor.add(*doctors)

            serializer = MappingSerializer(mapping)
            return Response(serializer.data, status=201)

        except Patient_Model.DoesNotExist:
            return Response({"error": "Patient not found"}, status=404)
        except Doctor_Model.DoesNotExist:
            return Response({"error": "One or more doctors not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
    
    def delete(self, request, pid,did = None):            
        try:    
            patient = Patient_Model.objects.get(id=pid)
            mapping = Mappings_Model.objects.get(patient=patient)
            if did is None:
                mapping.delete()
                return Response({"message": "Mapping deleted successfully"}, status=200)
            doctor = Doctor_Model.objects.get(id=did)
            mapping.doctor.remove(doctor)

            serializer = MappingSerializer(mapping)
            return Response(serializer.data, status=200)

        except Mappings_Model.DoesNotExist:
            return Response({"detail": "Mapping not found."}, status=404)
        except Doctor_Model.DoesNotExist:
            return Response({"detail": "Doctor not found."}, status=404)
        