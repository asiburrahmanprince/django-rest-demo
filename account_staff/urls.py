from django.urls import path
from .views import (
    AccountStaffListView,
    AccountStaffCreateView,
    AccountStaffUpdateView,
    AccountStaffDeleteView,
)

urlpatterns = [
    path('', AccountStaffListView.as_view(), name='accountstaff_list'),
    path('account-staff/add/', AccountStaffCreateView.as_view(), name='accountstaff_create'),
    path('account-staff/<int:pk>/edit/', AccountStaffUpdateView.as_view(), name='accountstaff_update'),
    path('account-staff/<int:pk>/delete/', AccountStaffDeleteView.as_view(), name='accountstaff_delete'),
]
