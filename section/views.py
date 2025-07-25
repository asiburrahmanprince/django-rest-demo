from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Section
from .forms import SectionForm
from school_class.models import SchoolClass

class SectionListView(ListView):
    model = Section
    template_name = 'section/section_list.html'
    context_object_name = 'sections'

    def get_queryset(self):
        queryset = super().get_queryset()
        class_name = self.request.GET.get('class_name')
        if class_name:
            queryset = queryset.filter(school_class__name=class_name)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = SchoolClass.objects.all()
        context['selected_class'] = self.request.GET.get('class_name', None)
        return context

class SectionCreateView(CreateView):
    model = Section
    form_class = SectionForm
    template_name = 'section/section_form.html'
    success_url = reverse_lazy('section_list')

class SectionUpdateView(UpdateView):
    model = Section
    form_class = SectionForm
    template_name = 'section/section_form.html'
    success_url = reverse_lazy('section_list')

class SectionDeleteView(DeleteView):
    model = Section
    template_name = 'section/section_confirm_delete.html'
    success_url = reverse_lazy('section_list')
