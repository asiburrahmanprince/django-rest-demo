from django.urls import path
from .views import (
    SchoolClassListView, SchoolClassCreateView, SchoolClassUpdateView, SchoolClassDeleteView
)

urlpatterns = [
    path('', SchoolClassListView.as_view(), name='class-list'),
    path('create/', SchoolClassCreateView.as_view(), name='class-create'),
    path('update/<int:pk>/', SchoolClassUpdateView.as_view(), name='class-update'),
    path('delete/<int:pk>/', SchoolClassDeleteView.as_view(), name='class-delete'),
]
