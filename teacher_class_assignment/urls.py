from django.urls import path
from .views import (
    TeacherClassAssignmentListView,
    TeacherClassAssignmentCreateView,
    TeacherClassAssignmentUpdateView,
    TeacherClassAssignmentDeleteView
)

urlpatterns = [
    path('', TeacherClassAssignmentListView.as_view(), name='assignment_list'),
    path('add/', TeacherClassAssignmentCreateView.as_view(), name='assignment_add'),
    path('edit/<int:pk>/', TeacherClassAssignmentUpdateView.as_view(), name='assignment_edit'),
    path('delete/<int:pk>/', TeacherClassAssignmentDeleteView.as_view(), name='assignment_delete'),
]
