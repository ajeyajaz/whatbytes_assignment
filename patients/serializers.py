from .models import Patient
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = "__all__"
        read_only_fields = ['added_by']




