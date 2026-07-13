import logging

from django.core.mail import send_mail
from django.conf import settings

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Employee
from .serializers import EmployeeSerializer
from .permissions import IsAdminOrHR

logger = logging.getLogger("employees")


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all().order_by("id")
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, IsAdminOrHR]

    filterset_fields = ["department", "designation"]

    search_fields = [
        "employee_id",
        "first_name",
        "last_name",
        "email",
    ]

    ordering_fields = [
        "salary",
        "joining_date",
        "employee_id",
    ]

    def perform_create(self, serializer):
        employee = serializer.save()

        logger.info(f"Employee created: {employee.employee_id}")

        send_mail(
            subject="Welcome to Company Portal",
            message=(
                f"Hello {employee.first_name},\n\n"
                "Your employee profile has been created successfully."
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[employee.email],
            fail_silently=True,
        )


class EmployeeRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, IsAdminOrHR]

    def perform_update(self, serializer):
        employee = serializer.save()
        logger.info(f"Employee updated: {employee.employee_id}")

    def perform_destroy(self, instance):
        logger.info(f"Employee deleted: {instance.employee_id}")
        instance.delete()