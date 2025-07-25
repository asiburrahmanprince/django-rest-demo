from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TeacherClassAssignment

class TeacherClassAssignmentListView(ListView):
    model = TeacherClassAssignment
    template_name = 'teacher_class_assignment/assignment_list.html'
    context_object_name = 'assignments'

class TeacherClassAssignmentCreateView(CreateView):
    model = TeacherClassAssignment
    fields = ['teacher', 'subject', 'school_class']
    template_name = 'teacher_class_assignment/assignment_form.html'
    success_url = reverse_lazy('assignment_list')

class TeacherClassAssignmentUpdateView(UpdateView):
    model = TeacherClassAssignment
    fields = ['teacher', 'subject', 'school_class']
    template_name = 'teacher_class_assignment/assignment_form.html'
    success_url = reverse_lazy('assignment_list')

class TeacherClassAssignmentDeleteView(DeleteView):
    model = TeacherClassAssignment
    template_name = 'teacher_class_assignment/assignment_confirm_delete.html'
    success_url = reverse_lazy('assignment_list')
