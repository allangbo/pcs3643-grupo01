from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'auth'

urlpatterns = [
    path('', auth_views.LoginView.as_view(
        template_name='users/login_form.html'
    ), name='login'),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login_form.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.CreateUser.as_view(), name='register'),
    path('auctioneer/new', views.auctioneer_create , name='auctioneer_new'),
    path('auctioneer/list', views.auctioneer_list, name='auctioneer_list'),
    path('auctioneer/deactivate/<int:user_id>/', views.auctioneer_deactivate, name='auctioneer_deactivate'),
    path('auctioneer/activate/<int:user_id>/', views.auctioneer_activate, name='auctioneer_activate'),
    path('seller_buyer/new', views.seller_buyer_create , name='seller_buyer_new'),
    path('seller_buyer/list', views.seller_buyer_list, name='seller_buyer_list'),
    path('seller_buyer/deactivate/<int:user_id>/', views.seller_buyer_deactivate, name='seller_buyer_deactivate'),
    path('seller_buyer/activate/<int:user_id>/', views.seller_buyer_activate, name='seller_buyer_activate'),
    path('manager/new', views.manager_create , name='manager_new'),
    path('manager/list', views.manager_list, name='manager_list'),
    path('manager/deactivate/<int:user_id>/', views.manager_deactivate, name='manager_deactivate'),
    path('manager/activate/<int:user_id>/', views.manager_activate, name='manager_activate')
]