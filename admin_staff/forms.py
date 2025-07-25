from django import forms
from .models import AdminStaff

class AdminStaffForm(forms.ModelForm):
    class Meta:
        model = AdminStaff
        fields = ['name', 'role']
