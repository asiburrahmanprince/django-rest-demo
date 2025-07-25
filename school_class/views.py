from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from  .models import SchoolClass


class SchoolClassListView(ListView):
    model = SchoolClass
    template_name = 'school/class_list.html'
    context_object_name = 'classes'

class SchoolClassCreateView(CreateView):
    model = SchoolClass
    template_name = 'school/class_form.html'
    fields = ['name']
    success_url = reverse_lazy('class-list')

class SchoolClassUpdateView(UpdateView):
    model = SchoolClass
    template_name = 'school/class_form.html'
    fields = ['name']
    success_url = reverse_lazy('class-list')

class SchoolClassDeleteView(DeleteView):
    model = SchoolClass
    template_name = 'school/class_confirm_delete.html'
    success_url = reverse_lazy('class-list')
