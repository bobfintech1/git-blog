from django.urls import path
from portfolio.views import *

app_name = 'portfolio'


urlpatterns = [
    path('', PortView.as_view(), name='port_page'),
    path('detail/<int:pk>', PortDetailView.as_view(), name="detail"),
    path('add/', PortAddView.as_view(), name="add"),
    path('update/<int:pk>/', PortUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', PortDeleteView.as_view(), name="delete"),


    path('create-port', create_port_view, name="create_port"),
    path('update-port/<int:id>/', update_port_view, name="update_port"),
]