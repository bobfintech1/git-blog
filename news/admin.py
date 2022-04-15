from django.contrib import admin
from news.models import NewsModel, ArticleModel
# Register your models here.



admin.site.register(NewsModel)

admin.site.register(ArticleModel)