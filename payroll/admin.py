from django.contrib import admin  # Import Django’s admin module
from .models import Employee, Payroll  # Import our models

admin.site.register(Employee)  # Register Employee model in the admin panel
admin.site.register(Payroll)  # Register Payroll model in the admin panel
