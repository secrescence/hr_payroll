from django.shortcuts import render, redirect
from .models import Employee, Payroll
from .forms import EmployeeForm


# View to display all employees
def employee_list(request):
    employees = Employee.objects.all()  # Get all employees from database
    return render(request, "payroll/employee_list.html", {"employees": employees})


# View to display all payroll records
def payroll_list(request):
    payrolls = Payroll.objects.all()  # Get all payroll records
    return render(request, "payroll/payroll_list.html", {"payrolls": payrolls})


# View for Adding Employees
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee_list")  # Redirect to employee list after saving
    else:
        form = EmployeeForm()

    return render(request, "payroll/add_employee.html", {"form": form})
