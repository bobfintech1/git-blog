from django.db import models
from datetime import date
from django.urls import reverse
# Create your models here.


class NewsModel(models.Model):
    title = models.CharField(max_length=15, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    primer = models.DateField('Date', default=date.today, null=True, blank=True)


    def __str__(self):
        return str(self.title)


    # def get_absolute_url(self):
    #     return reverse('news:detail', args=[str(self.id)])


