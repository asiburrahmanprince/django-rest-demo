from django.db import models

from school_class.models import SchoolClass
from subjects.models import Subject
from teacher.models import Teacher


class TeacherClassAssignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('teacher', 'subject', 'school_class')

    def __str__(self):
        return f"{self.teacher.name} teaches {self.subject.name} to Class {self.school_class.name}"
