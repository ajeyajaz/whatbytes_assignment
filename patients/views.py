from rest_framework import viewsets , permissions
from .serializers import PatientSerializer
from .models import Patient

class PatientViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PatientSerializer

    def get_queryset(self):
        return Patient.objects.filter(added_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)







