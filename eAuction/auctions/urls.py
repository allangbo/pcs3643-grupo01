from django.urls import path

from . import views

app_name = 'auctions'

urlpatterns = [
    path('', views.auction_list, name='auction_list'),
    path('new/', views.auction_create, name='auction_new'),
    path('edit/<int:pk>/', views.auction_update, name='auction_edit'),
    path('delete/<int:pk>/', views.auction_delete, name='auction_delete'),
    path('finish/<int:pk>/', views.auction_finish, name='auction_finish'),
    path('bid/<int:auction_id>/new', views.bid_create, name='bid_new'),
    path('bid/list', views.bid_list, name='bid_list')
]