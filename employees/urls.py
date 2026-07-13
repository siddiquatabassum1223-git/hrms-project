from django.urls import path
from .views import (
    EmployeeListCreateView,
    EmployeeRetrieveUpdateDestroyView,
)

urlpatterns = [
    path(
        "employees/",
        EmployeeListCreateView.as_view(),
        name="employee-list",
    ),

    path(
        "employees/<int:pk>/",
        EmployeeRetrieveUpdateDestroyView.as_view(),
        name="employee-detail",
    ),
]