from rest_framework import serializers
from .models import Mapping

class MappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mapping
        fields = ['patient','doctor','assigned_at']
        read_only_fields = ['assigned_at']


