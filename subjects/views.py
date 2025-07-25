from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Subject
from .forms import SubjectForm

class SubjectListView(ListView):
    model = Subject
    template_name = 'subject/subject_list.html'
    context_object_name = 'subjects'

class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subject/subject_form.html'
    success_url = reverse_lazy('subject-list')

class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subject/subject_form.html'
    success_url = reverse_lazy('subject-list')

class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'subject/subject_confirm_delete.html'
    success_url = reverse_lazy('subject-list')
