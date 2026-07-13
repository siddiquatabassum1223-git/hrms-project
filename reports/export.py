from django.http import HttpResponse
from openpyxl import Workbook

from employees.models import Employee


def export_employees_excel():
    workbook = Workbook()

    if workbook.active is None:
        worksheet = workbook.create_sheet(title="Employees")
    else:
        worksheet = workbook.active

    worksheet.title = "Employees"

    worksheet.append([
        "Employee ID",
        "First Name",
        "Last Name",
        "Email",
        "Phone",
        "Department",
        "Designation",
        "Salary",
        "Joining Date",
    ])

    for employee in Employee.objects.all():
        worksheet.append([
            employee.employee_id,
            employee.first_name,
            employee.last_name,
            employee.email,
            employee.phone,
            employee.department,
            employee.designation,
            float(employee.salary),
            str(employee.joining_date),
        ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="employees.xlsx"'

    workbook.save(response)
    return response
