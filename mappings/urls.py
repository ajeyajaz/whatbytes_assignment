from django.urls import path
from .views import MappingListCreateAPIView,DoctorListDestroyAPIView

urlpatterns = [
    path('',MappingListCreateAPIView.as_view(),name='mapping-list-create-api'),
    path('<int:pk>/',DoctorListDestroyAPIView.as_view(),name='doctor-list-delete-api')
]