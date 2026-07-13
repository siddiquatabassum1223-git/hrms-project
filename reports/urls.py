from django.urls import path

from .views import (
    ExportEmployeesExcelView,
    ExportEmployeesPDFView,
    ImportEmployeesExcelView,
    EmployeeIDCardView,
    DashboardView,
)

urlpatterns = [
    path(
        "employees/excel/",
        ExportEmployeesExcelView.as_view(),
        name="employees_excel",
    ),

    path(
        "employees/pdf/",
        ExportEmployeesPDFView.as_view(),
        name="employees_pdf",
    ),

    path(
        "employees/import/",
        ImportEmployeesExcelView.as_view(),
        name="employees_import",
    ),

    path(
        "id-card/<int:pk>/",
        EmployeeIDCardView.as_view(),
        name="employee_id_card",
    ),

    path(
        "dashboard/",
        DashboardView.as_view(),
        name="dashboard",
    ),
]