from django.db import models
from datetime import date
from django.urls import reverse
# Create your models here.


class ProjectModel(models.Model):
    title = models.CharField(max_length=15)
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    primer = models.DateField('Date', default=date.today)


    def __str__(self):
        return str(self.title)


    # def get_absolute_url(self):
    #     return reverse('project:detail', args=[str(self.id)])


class ProjectArticleModel(models.Model):
    title = models.CharField(max_length=15)
    body = models.TextField()
    primer = models.DateField('Date', default=date.today)


    def __str__(self):
        return str(self.title)