from django.db import models
from .validators import validate_image, validate_document


class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()

    profile_photo = models.ImageField(
        upload_to="employees/photos/",
        validators=[validate_image],
        blank=True,
        null=True,
    )

    resume = models.FileField(
        upload_to="employees/resumes/",
        validators=[validate_document],
        blank=True,
        null=True,
    )

    aadhaar_document = models.FileField(
        upload_to="employees/aadhaar/",
        validators=[validate_document],
        blank=True,
        null=True,
    )

    pan_document = models.FileField(
        upload_to="employees/pan/",
        validators=[validate_document],
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.employee_id} - {self.first_name} {self.last_name}"