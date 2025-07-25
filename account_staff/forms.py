from django import forms
from .models import AccountStaff

class AccountStaffForm(forms.ModelForm):
    class Meta:
        model = AccountStaff
        fields = ['name', 'role']
