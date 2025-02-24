from django import forms
from .models import Employee


# This form will handle employee creation.
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            "first_name",
            "last_name",
            "email",
            "position",
            "salary",
            "date_hired",
        ]
