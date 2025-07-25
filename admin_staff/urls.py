# admin_staff/urls.py
from django.urls import path
from .views import (
    AdminStaffListView, AdminStaffCreateView,
    AdminStaffUpdateView, AdminStaffDeleteView,
)

urlpatterns = [
    path('', AdminStaffListView.as_view(), name='adminstaff_list'),
    path('create/', AdminStaffCreateView.as_view(), name='adminstaff_create'),
    path('update/<int:pk>/', AdminStaffUpdateView.as_view(), name='adminstaff_update'),
    path('delete/<int:pk>/', AdminStaffDeleteView.as_view(), name='adminstaff_delete'),
]
