from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from project.models import ProjectModel
from news.models import NewsModel
from django.urls import reverse_lazy
# Create your views here.
from project.forms import CreateProjectForm

class ProjectViews(ListView):
    model = ProjectModel
    template_name = "project.html"



class ProjectDetailView(DetailView):
    model = ProjectModel
    template_name = 'news-porfolio-detail.html'
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


def create_project_form(request):

    context = {}

    form = CreateProjectForm(request.POST or None, request.FILES or None,)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = CreateProjectForm()

    context['form'] = form

    return render(request, "add.html", context)























# def project_list(request):
#     content = {}
#     project = ProjectModel.objects.all()
#     news = NewsModel.objects.all()
#     context = {
#         'project_list': project,
#         'news_list_one': news
#     }
#
#     return render(request, 'project_one.html', context)
#
