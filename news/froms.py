from django import forms
from news.models import *


class CreateArticleForm(forms.ModelForm):

    class Meta:
        model = ArticleModel
        fields = ["title", "body", "primer"]


class UpdateArticleForm(forms.ModelForm):

    class Meta:
        model = ArticleModel
        fields = ["title", "body", "primer"]


    def save(self, commit=True):
        article = self.instance
        article.title = self.cleaned_data['title']
        article.body = self.cleaned_data['body']


class DeleteArticleFrom(forms.ModelForm):

    class Meta:
        model = ArticleModel
        fields = ["title", "body", "primer"]


    def save(self, commit=True):
        article = self.instance
        article.title = self.cleaned_data['title']
        article.body = self.cleaned_data['body']
