from django.urls import path

from . import views

app_name = 'reports'

urlpatterns = [
    path('', views.create_report, name='create_report'),
]