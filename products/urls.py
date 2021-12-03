from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('new/', views.product_create, name='product_new'),
    path('edit/<int:pk>/', views.product_update, name='product_edit'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete')
]