from django.db import models

class AccountStaff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} (Accounts - {self.role})"
