from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import EmployeeDocument
from .serializers import EmployeeDocumentSerializer


class EmployeeDocumentListCreateView(
    generics.ListCreateAPIView
):
    queryset = EmployeeDocument.objects.all()
    serializer_class = EmployeeDocumentSerializer
    permission_classes = [IsAuthenticated]


class EmployeeDocumentRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = EmployeeDocument.objects.all()
    serializer_class = EmployeeDocumentSerializer
    permission_classes = [IsAuthenticated]