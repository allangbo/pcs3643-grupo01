from django.urls import path

from batches import views

app_name = 'batches'

urlpatterns = [
  path('', views.batch_list, name='batch_list'),
  path('new/', views.batch_create, name='batch_new'),
  path('edit/<int:pk>/', views.batch_update, name='batch_edit'),
  path('delete/<int:pk>/', views.batch_delete, name='batch_delete'),
]