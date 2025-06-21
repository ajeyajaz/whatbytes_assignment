import re
from django.contrib.auth import  password_validation
from .models import User
from rest_framework import serializers

# email validation
def validate_email(email):
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email):
        raise  serializers.ValidationError({"error": "Invalid email format"})

    if User.objects.filter(email__iexact=email).exists():
        raise serializers.ValidationError("Email already exists")
    return email

# password validation
def validate_password(password):
    password_validation.validate_password(password)
    return password


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    email = serializers.EmailField(validators=[validate_email])

    class Meta:
        model = User
        fields = ['email', 'name', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user












