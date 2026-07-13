from io import BytesIO

from django.http import HttpResponse

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

from employees.models import Employee


def export_employees_pdf():
    buffer = BytesIO()

    document = SimpleDocTemplate(buffer, pagesize=A4)

    data = [[
        "Employee ID",
        "First Name",
        "Last Name",
        "Department",
        "Designation",
        "Salary",
    ]]

    for employee in Employee.objects.all():
        data.append([
            employee.employee_id,
            employee.first_name,
            employee.last_name,
            employee.department,
            employee.designation,
            str(employee.salary),
        ])

    table = Table(data)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
    ]))

    document.build([table])

    pdf = buffer.getvalue()
    buffer.close()

    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="employees.pdf"'

    return response