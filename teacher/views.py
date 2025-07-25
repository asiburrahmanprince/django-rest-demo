from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Teacher
from .forms import TeacherForm
from teacher_subject.models import TeacherSubject

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher/teacher_list.html'
    context_object_name = 'teachers'


class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teacher/teacher_form.html'
    success_url = reverse_lazy('teacher_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        subjects = form.cleaned_data['subjects']
        for subject in subjects:
            TeacherSubject.objects.get_or_create(teacher=self.object, subject=subject)
        return response


class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teacher/teacher_form.html'
    success_url = reverse_lazy('teacher_list')

    def get_initial(self):
        initial = super().get_initial()
        initial['subjects'] = self.object.subjects.all()
        return initial

    def form_valid(self, form):
        TeacherSubject.objects.filter(teacher=self.object).delete()
        response = super().form_valid(form)
        subjects = form.cleaned_data['subjects']
        for subject in subjects:
            TeacherSubject.objects.get_or_create(teacher=self.object, subject=subject)
        return response


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teacher/teacher_confirm_delete.html'
    success_url = reverse_lazy('teacher_list')
