from django.db.models import Avg, Max
from employees.models import Employee


def get_dashboard_data():
    total_employees = Employee.objects.count()

    department_wise_count = {}

    for employee in Employee.objects.all():
        department = employee.department

        if department not in department_wise_count:
            department_wise_count[department] = 0

        department_wise_count[department] += 1

    highest_salary = Employee.objects.aggregate(
        Max("salary")
    )["salary__max"]

    average_salary = Employee.objects.aggregate(
        Avg("salary")
    )["salary__avg"]

    return {
        "total_employees": total_employees,
        "department_wise_count": department_wise_count,
        "highest_salary": highest_salary,
        "average_salary": average_salary,
    }