from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from portfolio.models import *
from django.urls import reverse_lazy
from portfolio.forms import CreatePortView, UpdatePortForm
# Create your views here.


class PortView(ListView):
    model = PortModels
    template_name = 'page/portfolio.html'



class PortDetailView(DetailView):
    model = PortModels
    template_name = 'page/porfolio-detail.html'
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


def create_port_view(request):

    context = {}

    form = CreatePortView(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = CreatePortView()

    context['form'] = form

    return render(request, 'add.html', context)


def update_port_view(request, id):
    context = {}

    port = get_object_or_404(ArticlePortModel, id=id)

    if request.POST:
        form = UpdatePortForm(request.POST or None, request.FILES or None, instance=port)
        if form.is_valid():
            obj = form.save(commit=True)
            obj.save()
            context['success_message'] = "Updated"
            port = obj

    form = UpdatePortForm(
        initial={
            "title": port.title,
            "body": port.body,
            "primer": port.primer,

        }
    )

    context['form'] = form
    return render(request, 'update.html', context)