from django.contrib.auth import password_validation
from .models import User
from rest_framework import serializers


#register serializer
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name','last_name', 'password','confirm_password']

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']: #match password
            raise serializers.ValidationError({'detail':'Both password fields must match'})
        password_validation.validate_password(attrs['password']) #check password is strong

        attrs.pop('confirm_password')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

















