from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from school_class.models import SchoolClass
from .models import Subject
from .forms import SubjectForm

class SubjectListView(ListView):
    model = Subject
    template_name = 'subject/subject_list.html'
    context_object_name = 'subjects'

    def get_queryset(self):
        class_id = self.request.GET.get('class_id')
        if class_id:
            return Subject.objects.filter(classes__id=class_id)
        return Subject.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_classes'] = SchoolClass.objects.all()
        return context

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
