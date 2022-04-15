from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from news.models import NewsModel, ArticleModel
from django.urls import reverse_lazy
from news.froms import CreateArticleForm, UpdateArticleForm, DeleteArticleFrom


# Create your views here.


class NewsViews(ListView):
    model = NewsModel
    template_name = "news.html"
    # context_object_name = 'news_list'


class NewsDetailView(DetailView):
    model = NewsModel
    template_name = 'news-detail.html'
    context_object_name = 'news1'


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


def create_article_view(request):

    context = {}

    form = CreateArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = CreateArticleForm()

    context['form'] = form

    return render(request, 'add.html', context)


def update_article_view(request, id):
    context = {}

    article = get_object_or_404(ArticleModel, id=id)

    if request.POST:
        form = UpdateArticleForm(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            form.save()
            # obj.save()
            context['success_message'] = "Updated"

    form = UpdateArticleForm(
        initial={
            'title': article.title,
            'body': article.body,
            'primer': article.primer,
        }
    )

    context['form'] = form
    return render(request, 'update.html', context)

def delete_article_view(request, id):

    context = {}

    article = get_object_or_404(ArticleModel, id=id)

    if request.POST:
        form = DeleteArticleFrom(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            obj = form.save(commit=True)
            obj.save()
            context['success_message'] = "Updated"
            article = obj

    form = DeleteArticleFrom(
        initial={
            'title': article.title,
            'body': article.body,
            'primer': article.primer,
        }
    )

    context['form'] = form
    return render(request, 'delete.html', context)



