# admin_staff/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import AdminStaff
from .forms import AdminStaffForm

class AdminStaffListView(ListView):
    model = AdminStaff
    template_name = 'admin_staff/adminstaff_list.html'
    context_object_name = 'adminstaffs'

class AdminStaffCreateView(CreateView):
    model = AdminStaff
    form_class = AdminStaffForm
    template_name = 'admin_staff/adminstaff_form.html'
    success_url = reverse_lazy('adminstaff_list')

class AdminStaffUpdateView(UpdateView):
    model = AdminStaff
    form_class = AdminStaffForm
    template_name = 'admin_staff/adminstaff_form.html'
    success_url = reverse_lazy('adminstaff_list')

class AdminStaffDeleteView(DeleteView):
    model = AdminStaff
    template_name = 'admin_staff/adminstaff_confirm_delete.html'
    success_url = reverse_lazy('adminstaff_list')
