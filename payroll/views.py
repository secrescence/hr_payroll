from django.shortcuts import render
from .models import Employee, Payroll


# View to display all employees
def employee_list(request):
    employees = Employee.objects.all()  # Get all employees from database
    return render(request, "payroll/employee_list.html", {"employees": employees})


# View to display all payroll records
def payroll_list(request):
    payrolls = Payroll.objects.all()  # Get all payroll records
    return render(request, "payroll/payroll_list.html", {"payrolls": payrolls})
