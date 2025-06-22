from rest_framework import  generics, permissions , views,serializers, status
from .serializers import MappingSerializer
from .models import Mapping
from rest_framework.response import Response

class MappingListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MappingSerializer
    queryset = Mapping.objects.all()

class DoctorListDestroyAPIView(views.APIView):

    def get_permissions(self):
        if self.request.method.lower() == "delete":
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def get_object(self, pk):
        mappings = Mapping.objects.filter(patient__id=pk)
        if not mappings.exists():
            raise serializers.ValidationError({'detail': 'No mappings found for this patient'})
        return mappings

    def get(self, request, pk):
        mappings = self.get_object(pk)
        serializer = MappingSerializer(mappings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        mappings = self.get_object(pk)
        mappings.delete()
        return Response(
            {'message': 'mappings deleted'},
            status=status.HTTP_204_NO_CONTENT
        )












