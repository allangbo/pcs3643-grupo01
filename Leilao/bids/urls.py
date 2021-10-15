from django.urls import path

from bids import views

app_name = 'bids'

urlpatterns = [
  path('', views.bid_list, name='bid_list'),
  path('new/', views.bid_create, name='bid_new'),
  path('edit/<int:pk>/', views.bid_update, name='bid_edit'),
  path('delete/<int:pk>/', views.bid_delete, name='bid_delete'),
]