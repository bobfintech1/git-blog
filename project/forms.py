from django import forms
from project.models import *


class CreateProjectForm(forms.ModelForm):

    class Meta:
        model = ProjectArticleModel
        fields = ['title', 'body', 'primer']


