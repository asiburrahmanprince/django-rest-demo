from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import AccountStaff
from .forms import AccountStaffForm

class AccountStaffListView(ListView):
    model = AccountStaff
    template_name = 'accountstaff/accountstaff_list.html'
    context_object_name = 'accountstaffs'

class AccountStaffCreateView(CreateView):
    model = AccountStaff
    form_class = AccountStaffForm
    template_name = 'accountstaff/accountstaff_form.html'
    success_url = reverse_lazy('accountstaff_list')

class AccountStaffUpdateView(UpdateView):
    model = AccountStaff
    form_class = AccountStaffForm
    template_name = 'accountstaff/accountstaff_form.html'
    success_url = reverse_lazy('accountstaff_list')

class AccountStaffDeleteView(DeleteView):
    model = AccountStaff
    template_name = 'accountstaff/accountstaff_confirm_delete.html'
    success_url = reverse_lazy('accountstaff_list')
