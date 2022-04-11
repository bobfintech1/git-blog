from django.urls import path
from portfolio.views import *

app_name = 'portfolio'


urlpatterns = [
    path('', PortView.as_view(), name='port_page'),
    path('detail/<int:pk>', PortDetailView.as_view(), name="detail"),
    path('add/', PortAddView.as_view(), name="add"),
    path('update/<int:pk>/', PortUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', PortDeleteView.as_view(), name="delete"),
]