from django.db import models
from subjects.models import Subject


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject, through='teacher_subject.TeacherSubject')

    def __str__(self):
        return self.name