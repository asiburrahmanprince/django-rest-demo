from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class SchoolClass(models.Model):
    name = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        unique=True
    )

    def __str__(self):
        return f"Class {self.name}"
