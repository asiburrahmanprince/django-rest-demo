from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Staff

class StaffListView(ListView):
    model = Staff
    template_name = 'staff/staff_list.html'
    context_object_name = 'staff_list'

class StaffCreateView(CreateView):
    model = Staff
    fields = ['name', 'job_description']
    template_name = 'staff/staff_form.html'
    success_url = reverse_lazy('staff-list')

class StaffUpdateView(UpdateView):
    model = Staff
    fields = ['name', 'job_description']
    template_name = 'staff/staff_form.html'
    success_url = reverse_lazy('staff-list')

class StaffDeleteView(DeleteView):
    model = Staff
    template_name = 'staff/staff_confirm_delete.html'
    success_url = reverse_lazy('staff-list')
