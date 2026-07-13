import os
import qrcode

from django.conf import settings
from employees.models import Employee


def generate_employee_qr(employee: Employee) -> str:
    qr_data = (
        f"Employee ID: {employee.employee_id}\n"
        f"Name: {employee.first_name} {employee.last_name}\n"
        f"Department: {employee.department}\n"
        f"Designation: {employee.designation}\n"
        f"Email: {employee.email}"
    )

    img = qrcode.make(qr_data)

    qr_folder = os.path.join(settings.MEDIA_ROOT, "qr_codes")
    os.makedirs(qr_folder, exist_ok=True)

    file_path = os.path.join(
        qr_folder,
        f"{employee.employee_id}.png"
    )

    with open(file_path, "wb") as file:
        img.save(file, "PNG")

    return file_path