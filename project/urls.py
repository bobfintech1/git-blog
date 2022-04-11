from django.urls import path
from project.views import *

app_name = 'project'


urlpatterns = [
    path('', ProjectViews.as_view(), name='project_page'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name="detail"),
    path('add/', ProjectAddView.as_view(), name="add"),
    path('update/<int:pk>/', ProjectUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', ProjectDeleteView.as_view(), name="delete"),
]
