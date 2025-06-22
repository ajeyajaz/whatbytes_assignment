from django.urls import path,include
from rest_framework.routers import SimpleRouter
from .views import DoctorViewSet

router= SimpleRouter()
router.register('',DoctorViewSet,basename='doctor')

urlpatterns = [
    path('',include(router.urls))
]