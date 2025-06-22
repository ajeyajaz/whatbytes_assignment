from rest_framework.generics import CreateAPIView
from .serializers import UserRegisterSerializer

class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer





