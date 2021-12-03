from django.contrib import admin
from django.urls import include, path
from . import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', include('theme.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
