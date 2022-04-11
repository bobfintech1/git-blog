from django.urls import path
from small.views import *

app_name = 'small'


urlpatterns = [
    path('', WorkView.as_view(), name='small-list'),
    path('detail/<int:pk>', WorkDetailView.as_view(), name="detail"),
    path('add/', WorkAddView.as_view(), name="add"),
    path('update/<int:pk>/', WorkUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', WorkDeleteView.as_view(), name="delete")
]