from django import forms
from .models import Section

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name', 'school_class', 'medium']
