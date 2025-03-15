
from rest_framework.views import APIView
from .models import Patient_Model
from .serializers import PatientSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class Patient_View(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id=None):
        if id:
            try:
                patient = Patient_Model.objects.get(id=id)
                serializer = PatientSerializer(patient)
                return Response(serializer.data, status=200)
            except Patient_Model.DoesNotExist:
                return Response({"error": "Patient not found"}, status=404)
        else:
            patients = Patient_Model.objects.all()
            serializer = PatientSerializer(patients, many=True)
            return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
        
    def put(self, request, id = None):
        if id is None:
            return Response({"error": "Please enter a valid id"}, status=400)
        try:
            patient = Patient_Model.objects.get(id=id)
            serializer = PatientSerializer(patient, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response(serializer.errors, status=400)
        except Patient_Model.DoesNotExist:
            return Response({"error": "Patient not found"}, status=404)
        
    def delete(self, request, id):
        if id is None:
            return Response({"error": "Please enter a valid id"}, status=400)
        try:
            patient = Patient_Model.objects.get(id=id)
            patient.delete()
            return Response({"message": "Patient deleted successfully"}, status=200)
        except Patient_Model.DoesNotExist:
            return Response({"error": "Patient not found"}, status=404)
        