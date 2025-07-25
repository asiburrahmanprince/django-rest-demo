from django.db import models
from school_class.models import SchoolClass


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    classes = models.ManyToManyField(SchoolClass)

    def __str__(self):
        return self.name