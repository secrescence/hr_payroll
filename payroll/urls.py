from django.urls import path
from .views import (
    employee_list,
    payroll_list,
    add_employee,
    edit_employee,
    delete_employee,
    employee_detail,
)

urlpatterns = [
    path("employees/", employee_list, name="employee_list"),
    path("payrolls/", payroll_list, name="payroll_list"),
    path("employees/add/", add_employee, name="add_employee"),
    path("employees/edit/<int:pk>/", edit_employee, name="edit_employee"),
    path("employees/delete/<int:id>/", delete_employee, name="delete_employee"),
    path("employees/<int:employee_id>/", employee_detail, name="employee_detail"),
]
