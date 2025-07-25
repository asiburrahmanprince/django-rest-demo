from django.urls import path
from .views import (
    SubjectListView, SubjectCreateView, SubjectUpdateView, SubjectDeleteView
)

urlpatterns = [
    path('', SubjectListView.as_view(), name='subject-list'),
    path('subjects/add/', SubjectCreateView.as_view(), name='subject-add'),
    path('subjects/edit/<int:pk>/', SubjectUpdateView.as_view(), name='subject-edit'),
    path('subjects/delete/<int:pk>/', SubjectDeleteView.as_view(), name='subject-delete'),
]
