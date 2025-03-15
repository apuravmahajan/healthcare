from rest_framework.views import APIView
from .models import Doctor_Model
from .serializers import DoctorSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class Doctor_View(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id=None):
        if id:
            try:
                doctor = Doctor_Model.objects.get(id=id)
                serializer = DoctorSerializer(doctor)
                return Response(serializer.data, status=200)
            except Doctor_Model.DoesNotExist:
                return Response({"error": "Doctor not found"}, status=404)
        else:
            doctors = Doctor_Model.objects.all()
            serializer = DoctorSerializer(doctors, many=True)
            return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
        
    def put(self, request, id = None):
        if id is None:
            return Response({"error": "Please enter a valid id"}, status=400)
        try:
            doctor = Doctor_Model.objects.get(id=id)
            serializer = DoctorSerializer(doctor, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response(serializer.errors, status=400)
        except Doctor_Model.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=404)
        
    def delete(self, request, id):
        if id is None:
            return Response({"error": "Please enter a valid id"}, status=400)
        try:
            doctor = Doctor_Model.objects.get(id=id)
            doctor.delete()
            return Response({"message": "Doctor deleted successfully"}, status=200)
        except Doctor_Model.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=404)
        