from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

from .export import export_employees_excel
from .pdf import export_employees_pdf
from .import_excel import import_employees
from .id_card import generate_id_card
from .dashboard import get_dashboard_data


class ExportEmployeesExcelView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return export_employees_excel()


class ExportEmployeesPDFView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return export_employees_pdf()


class ImportEmployeesExcelView(APIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser]

    def post(self, request):
        excel_file = request.FILES.get("file")

        if not excel_file:
            return Response(
                {"error": "No file uploaded."},
                status=400,
            )

        import_employees(excel_file)

        return Response(
            {"message": "Employees imported successfully."},
            status=200,
        )


class EmployeeIDCardView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        return generate_id_card(pk)


class DashboardView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response(get_dashboard_data())