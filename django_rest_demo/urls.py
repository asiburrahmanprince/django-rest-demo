from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classes/', include('school_class.urls')),
    path('subjects/', include('subjects.urls')),
    path('teachers/', include('teacher.urls')),
    path('assignments/', include('teacher_class_assignment.urls')),
    path('teacher_subjects/', include('teacher_subject.urls')),
    path('sections/', include('section.urls')),
    path('students/', include('student.urls')),

]
