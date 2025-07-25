from django.db import models
from subjects.models import Subject

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True, null=True)  # New field added
    subjects = models.ManyToManyField(Subject, through='teacher_subject.TeacherSubject')

    def __str__(self):
        if self.designation:
            return f"{self.name} ({self.designation})"
        return self.name