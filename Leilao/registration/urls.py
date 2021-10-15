from django.urls import path

from registration import views

app_name = 'registration'

urlpatterns = [
  path('', views.registration_login, name='registration_login'),
]