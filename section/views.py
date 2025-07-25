from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Section
from .forms import SectionForm

class SectionListView(ListView):
    model = Section
    template_name = 'section/section_list.html'
    context_object_name = 'sections'

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
