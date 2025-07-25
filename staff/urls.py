from django.urls import path
from .views import StaffListView, StaffCreateView, StaffUpdateView, StaffDeleteView

urlpatterns = [
    path('', StaffListView.as_view(), name='staff-list'),
    path('add/', StaffCreateView.as_view(), name='staff-add'),
    path('edit/<int:pk>/', StaffUpdateView.as_view(), name='staff-edit'),
    path('delete/<int:pk>/', StaffDeleteView.as_view(), name='staff-delete'),
]
