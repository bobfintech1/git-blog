from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from portfolio.models import *
from django.urls import reverse_lazy
# Create your views here.


class PortView(ListView):
    model = PortModels
    template_name = 'page/portfolio.html'



class PortDetailView(DetailView):
    model = PortModels
    template_name = 'page/detail.html'
    context_object_name = 'portfolio'

class PortAddView(CreateView):
    model = PortModels
    template_name = 'page/add.html'
    fields = ['title', 'body', 'author', 'primer']

class PortUpdateView(UpdateView):
    model = PortModels
    template_name = 'page/update.html'
    fields = ['title', 'body', 'primer']


class PortDeleteView(DeleteView):
    model = PortModels
    template_name = 'page/delete.html'
    context_object_name = 'portfolio'
    success_url = reverse_lazy('portfolio:port_page')