from django.urls import path
from .views import (
    SectionListView,
    SectionCreateView,
    SectionUpdateView,
    SectionDeleteView
)

urlpatterns = [
    path('', SectionListView.as_view(), name='section_list'),
    path('add/', SectionCreateView.as_view(), name='section_add'),
    path('edit/<int:pk>/', SectionUpdateView.as_view(), name='section_edit'),
    path('delete/<int:pk>/', SectionDeleteView.as_view(), name='section_delete'),
]
