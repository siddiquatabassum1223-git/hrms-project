from django.urls import path

from .views import (
    EmployeeDocumentListCreateView,
    EmployeeDocumentRetrieveUpdateDestroyView,
)

urlpatterns = [
    path(
        "documents/",
        EmployeeDocumentListCreateView.as_view(),
        name="document-list",
    ),

    path(
        "documents/<int:pk>/",
        EmployeeDocumentRetrieveUpdateDestroyView.as_view(),
        name="document-detail",
    ),
]