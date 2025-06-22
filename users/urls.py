from django.urls import path
from .views import UserRegisterAPIView

from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='register-api'),
    path('login/',TokenObtainPairView.as_view(), name='login'),

]