from django.urls import path

from sellers import views

app_name = 'sellers'

urlpatterns = [
  path('', views.seller_list, name='seller_list'),
  path('new/', views.seller_create, name='seller_new'),
  path('edit/<int:pk>/', views.seller_update, name='seller_edit'),
  path('delete/<int:pk>/', views.seller_delete, name='seller_delete'),
]