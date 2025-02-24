from django.urls import path
from .views import employee_list, payroll_list, add_employee

urlpatterns = [
    path("employees/", employee_list, name="employee_list"),
    path("payrolls/", payroll_list, name="payroll_list"),
    path("employees/add/", add_employee, name="add_employee"),
]
