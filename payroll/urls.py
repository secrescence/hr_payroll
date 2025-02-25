from django.urls import path
from .views import employee_list, payroll_list, add_employee, edit_employee

urlpatterns = [
    path("employees/", employee_list, name="employee_list"),
    path("payrolls/", payroll_list, name="payroll_list"),
    path("employees/add/", add_employee, name="add_employee"),
    path("employees/edit/<int:pk>/", edit_employee, name="edit_employee"),
]
