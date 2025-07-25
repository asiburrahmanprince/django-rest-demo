from django.db import models
from subjects.models import Subject

class Teacher(models.Model):
    DESIGNATION_CHOICES = (
        ("Assistant Teacher", "Assistant Teacher"),
        ("Senior Teacher", "Senior Teacher"),
        ("Head Teacher", "Head Teacher"),
        ("Subject Teacher", "Subject Teacher"),
        ("ICT Teacher", "ICT Teacher"),
        ("Physical Education Teacher", "Physical Education Teacher"),
        ("Library Teacher", "Library Teacher"),
        ("Art & Craft Teacher", "Art & Craft Teacher"),
        ("Lecturer", "Lecturer"),
        ("Senior Lecturer", "Senior Lecturer"),
        ("Assistant Professor", "Assistant Professor"),
        ("Associate Professor", "Associate Professor"),
        ("Professor", "Professor"),
        ("Principal", "Principal"),
        ("Vice Principal", "Vice Principal"),
    )

    name = models.CharField(max_length=100)
    designation = models.CharField(
        max_length=100,
        choices=DESIGNATION_CHOICES,
        blank=True,
        null=True
    )
    subjects = models.ManyToManyField(Subject, through='teacher_subject.TeacherSubject')

    def __str__(self):
        if self.designation:
            return f"{self.name} ({self.designation})"
        return self.name