from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
  path('', views.user_list, name='user_list'),
  path('new/', views.user_create, name='user_new'),
  path('edit/<int:pk>/', views.user_update, name='user_edit'),
  path('delete/<int:pk>/', views.user_delete, name='user_delete'),
]