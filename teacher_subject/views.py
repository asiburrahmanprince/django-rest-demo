from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TeacherSubject

class TeacherSubjectListView(ListView):
    model = TeacherSubject
    template_name = 'teacher_subject/teacher_subject_list.html'
    context_object_name = 'teacher_subjects'

class TeacherSubjectCreateView(CreateView):
    model = TeacherSubject
    fields = ['teacher', 'subject']
    template_name = 'teacher_subject/teacher_subject_form.html'
    success_url = reverse_lazy('teacher_subject_list')

class TeacherSubjectUpdateView(UpdateView):
    model = TeacherSubject
    fields = ['teacher', 'subject']
    template_name = 'teacher_subject/teacher_subject_form.html'
    success_url = reverse_lazy('teacher_subject_list')

class TeacherSubjectDeleteView(DeleteView):
    model = TeacherSubject
    template_name = 'teacher_subject/teacher_subject_confirm_delete.html'
    success_url = reverse_lazy('teacher_subject_list')
