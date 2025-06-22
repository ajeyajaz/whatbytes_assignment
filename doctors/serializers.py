from .models import Doctor
from rest_framework import serializers

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = "__all__"
        read_only_fields = ['added_by']

class DoctorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name','added_by']
        read_only_fields = ['added_by']






