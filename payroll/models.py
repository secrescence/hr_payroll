from django.db import models  # Import Django's database module


# Employee Model (Represents employees in the company)
class Employee(models.Model):
    first_name = models.CharField(max_length=100)  # Employee's first name
    last_name = models.CharField(max_length=100)  # Employee's last name
    email = models.EmailField(unique=True)  # Unique email
    position = models.CharField(max_length=100)  # Job position (e.g., Developer, HR)
    salary = models.DecimalField(max_digits=10, decimal_places=2)  # Monthly salary
    date_hired = models.DateField()  # Date the employee was hired

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  # This will be the default display for an Employee object


# Payroll Model (Represents salary payments)
class Payroll(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE
    )  # Links to an Employee
    month = models.CharField(max_length=20)  # Payroll month (e.g., January, February)
    year = models.IntegerField()  # Payroll year
    basic_salary = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # Employee's basic salary
    deductions = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )  # Salary deductions
    net_salary = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # Final salary after deductions

    def __str__(self):
        return f"Payroll for {self.employee.first_name} {self.employee.last_name} - {self.month} {self.year}"
