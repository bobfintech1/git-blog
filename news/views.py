from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from news.models import *
# Create your views here.

class NewsViews(ListView):
    model = NewsModel
    template_name = "news.html"
    # context_object_name = 'news_list'


class NewsDetailView(DetailView):
    model = NewsModel
    template_name = 'detail.html'
    # context_object_name = 'news1'

class NewsAddView(CreateView):
    model = NewsModel
    template_name = 'add.html'
    fields = ['title', 'body', 'author', 'primer']

class NewsUpdateView(UpdateView):
    model = NewsModel
    template_name = 'update.html'
    fields = ["title", "body", "primer"]


class NewsDeleteView(DetailView):
    model = NewsModel
    template_name = 'delete.html'
    context_object_name = 'news'
    success_url = reverse_lazy('news:news_page')