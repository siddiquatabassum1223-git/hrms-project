from django.db import models
from employees.models import Employee


class EmployeeDocument(models.Model):

    DOCUMENT_TYPES = [
        ("Resume", "Resume"),
        ("Aadhaar", "Aadhaar"),
        ("PAN", "PAN"),
        ("Degree Certificate", "Degree Certificate"),
        ("Experience Certificate", "Experience Certificate"),
        ("Offer Letter", "Offer Letter"),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="documents"
    )

    document_name = models.CharField(max_length=100)

    document_type = models.CharField(
        max_length=50,
        choices=DOCUMENT_TYPES
    )

    file = models.FileField(
        upload_to="documents/"
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.document_name