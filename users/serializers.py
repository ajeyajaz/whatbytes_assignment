from tkinter.font import names

from .models import User

from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50,allow_blank=False)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user











