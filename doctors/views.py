from .serializers import DoctorSerializer, DoctorListSerializer
from rest_framework import  permissions, viewsets
from .pemissions import IsOwnerOrReadonly
from .models import Doctor


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsOwnerOrReadonly]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return DoctorListSerializer
        return DoctorSerializer

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)






