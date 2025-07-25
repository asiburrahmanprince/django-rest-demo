from django.urls import path
from .views import (
    TeacherSubjectListView,
    TeacherSubjectCreateView,
    TeacherSubjectUpdateView,
    TeacherSubjectDeleteView
)

urlpatterns = [
    path('', TeacherSubjectListView.as_view(), name='teacher_subject_list'),
    path('create/', TeacherSubjectCreateView.as_view(), name='teacher_subject_create'),
    path('edit/<int:pk>/', TeacherSubjectUpdateView.as_view(), name='teacher_subject_edit'),
    path('delete/<int:pk>/', TeacherSubjectDeleteView.as_view(), name='teacher_subject_delete'),
]
