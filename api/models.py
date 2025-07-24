from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# ----------------------------
# Constants
# ----------------------------

MEDIUM_CHOICES = (
    ('bangla', 'Bangla Medium'),
    ('english', 'English Medium'),
)

# ----------------------------
# School Class (Class 1 to 10)
# ----------------------------

class SchoolClass(models.Model):
    name = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        unique=True
    )

    def __str__(self):
        return f"Class {self.name}"

# ----------------------------
# Section (Each class has 10 sections)
# ----------------------------

class Section(models.Model):
    name = models.CharField(max_length=1)  # e.g., A, B, C, D...
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, related_name='sections')
    medium = models.CharField(max_length=10, choices=MEDIUM_CHOICES)

    class Meta:
        unique_together = ('school_class', 'name')

    def __str__(self):
        return f"{self.school_class} - Section {self.name} ({self.medium})"

# ----------------------------
# Student
# ----------------------------

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.PositiveIntegerField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='students')

    class Meta:
        unique_together = ('roll_number', 'section')

    def __str__(self):
        return f"{self.name} (Roll: {self.roll_number})"

# ----------------------------
# Subject
# ----------------------------

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# ----------------------------
# Teacher
# ----------------------------

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject, through='TeacherSubject')

    def __str__(self):
        return self.name

# ----------------------------
# TeacherSubject (Mapping between teacher and subject)
# ----------------------------

class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('teacher', 'subject')

    def __str__(self):
        return f"{self.teacher.name} - {self.subject.name}"

# ----------------------------
# TeacherClassAssignment (Teacher teaches subject to class)
# ----------------------------

class TeacherClassAssignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('teacher', 'subject', 'school_class')

    def __str__(self):
        return f"{self.teacher.name} teaches {self.subject.name} to Class {self.school_class.name}"

# ----------------------------
# Staff (Cleaning, Maintenance)
# ----------------------------

class Staff(models.Model):
    name = models.CharField(max_length=100)
    job_description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.job_description}"

# ----------------------------
# Admin Staff
# ----------------------------

class AdminStaff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} (Admin - {self.role})"

# ----------------------------
# Account Staff
# ----------------------------

class AccountStaff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} (Accounts - {self.role})"
