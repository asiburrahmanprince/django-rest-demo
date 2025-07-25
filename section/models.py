from django.db import models
from school_class.models import SchoolClass


MEDIUM_CHOICES = (
    ('bangla', 'Bangla Medium'),
    ('english', 'English Medium'),
)


class Section(models.Model):
    name = models.CharField(max_length=1)  # e.g., A, B, C, D...
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, related_name='sections')
    medium = models.CharField(max_length=10, choices=MEDIUM_CHOICES)

    class Meta:
        unique_together = ('school_class', 'name')

    def __str__(self):
        return f"{self.school_class} - Section {self.name} ({self.medium})"
