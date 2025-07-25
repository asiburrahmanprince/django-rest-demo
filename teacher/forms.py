from django import forms
from .models import Teacher
from subjects.models import Subject

class TeacherForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Teacher
        fields = ['name', 'subjects']
