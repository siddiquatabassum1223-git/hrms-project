from openpyxl import Workbook
from django.http import HttpResponse
from .models import EmployeeDocument


def export_documents_excel(request):
    # Create workbook
    workbook = Workbook()

    # Get active worksheet
    worksheet = workbook.active
    if worksheet is None:
        worksheet = workbook.create_sheet(title="Employee Documents")

    worksheet.title = "Employee Documents"

    # Header row
    worksheet.append([
        "ID",
        "Employee",
        "Document Name",
        "Document Type",
        "Uploaded At",
    ])

    # Fetch all documents
    documents = EmployeeDocument.objects.select_related("employee").all()

    # Write data
    for document in documents:
        worksheet.append([
            document.pk,
            str(document.employee),
            document.document_name,
            document.document_type,
            document.uploaded_at.strftime("%Y-%m-%d %H:%M:%S"),
        ])

    # Create response
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = (
        'attachment; filename="employee_documents.xlsx"'
    )

    # Save workbook to response
    workbook.save(response)

    return response