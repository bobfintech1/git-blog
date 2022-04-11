from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from project.models import *
from django.urls import reverse_lazy
# Create your views here.

class ProjectViews(ListView):
    model = ProjectModel
    template_name = "project.html"



class ProjectDetailView(DetailView):
    model = ProjectModel
    template_name = 'detail.html'
    context_object_name = 'project'

class ProjectAddView(CreateView):
    model = ProjectModel
    template_name = 'add.html'
    fields = ['title', 'body', 'author', 'primer']

class ProjectUpdateView(UpdateView):
    model = ProjectModel
    template_name = 'update.html'
    fields = ["title", "body", "primer"]


class ProjectDeleteView(DeleteView):
    model = ProjectModel
    template_name = 'delete.html'
    context_object_name = 'project'
    success_url = reverse_lazy('project:project_page')