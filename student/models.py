from django.db import models

from section.models import Section


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.PositiveIntegerField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='students')

    class Meta:
        unique_together = ('roll_number', 'section')

    def __str__(self):
        return f"{self.name} (Roll: {self.roll_number})"
