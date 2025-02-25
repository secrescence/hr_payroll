from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Payroll
from .forms import EmployeeForm


# View to display all employees
def employee_list(request):
    query = request.GET.get("q", "")  # Get search query from URL
    if query:
        employees = Employee.objects.filter(
            first_name__icontains=query
        ) | Employee.objects.filter(last_name__icontains=query)
    else:
        employees = Employee.objects.all()
    return render(
        request, "payroll/employee_list.html", {"employees": employees, "query": query}
    )


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


# View to edit employee details
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        employee.first_name = request.POST["first_name"]
        employee.last_name = request.POST["last_name"]
        employee.email = request.POST["email"]
        employee.position = request.POST["position"]
        employee.salary = request.POST["salary"]
        employee.date_hired = request.POST["date_hired"]
        employee.save()
        return redirect("employee_list")

    return render(request, "payroll/edit_employee.html", {"employee": employee})


# View to delete employee
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect("employee_list")


# View to display employee details
def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, "payroll/employee_detail.html", {"employee": employee})
