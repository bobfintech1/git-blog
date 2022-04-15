from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from small.models import *
from django.urls import reverse_lazy
# Create your views here.

class WorkView(ListView):
    model = WorkModel
    template_name = 'page/build.html'


class WorkDetailView(DetailView):
    model = WorkModel
    template_name = 'page/news-porfolio-detail.html'
    context_object_name = 'small'

class WorkAddView(CreateView):
    model = WorkModel
    template_name = 'page/add.html'
    fields = ['title', 'body', 'author', 'primer']

class WorkUpdateView(UpdateView):
    model = WorkModel
    template_name = 'page/update.html'
    fields = ["title", "body", "primer"]


class WorkDeleteView(DeleteView):
    model = WorkModel
    template_name = 'page/delete.html'
    context_object_name = 'small'
    success_url = reverse_lazy('small:small-list')