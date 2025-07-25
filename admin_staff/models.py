from django.db import models

class AdminStaff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} (Admin - {self.role})"
