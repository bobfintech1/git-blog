from django.urls import path
from news.views import *

app_name = 'news'


urlpatterns = [
    path('', NewsViews.as_view(), name='news_page'),
    path('detail/<int:pk>', NewsDetailView.as_view(), name="detail"),
    path('add/', NewsAddView.as_view(), name="add"),
    path('update/<int:pk>/', NewsUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', NewsDeleteView.as_view(), name="delete")
]