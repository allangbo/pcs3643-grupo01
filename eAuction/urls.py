from django.contrib import admin
from django.urls import include, path
from . import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', include('theme.urls')),
    path('auth/', include('users.urls')),
    path('auctions/', include('auctions.urls')),
    path('products/', include('products.urls')),  
    path('batches/', include('batches.urls')),  
    path('reports/', include('reports.urls')),  
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
