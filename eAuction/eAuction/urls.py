from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('theme.urls')),
    path('auth/', include('users.urls')),
    path('auctions/', include('auctions.urls')),
    path('products/', include('products.urls')),  
    path('batches/', include('batches.urls')),  
    path('reports/', include('reports.urls')),  
    path('admin/', admin.site.urls),
]
