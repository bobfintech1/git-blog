from django import forms
from portfolio.models import *


class CreatePortView(forms.ModelForm):

    class Meta:
        model = ArticlePortModel
        fields = ['title', "body", "primer"]


class UpdatePortForm(forms.ModelForm):

    class Meta:
        model = ArticlePortModel
        fields = ['title', "body", "primer"]

    def save(self, commit=True):
        port = self.instance
        port.title = self.cleaned_data['title']
        port.body = self.cleaned_data['body']
