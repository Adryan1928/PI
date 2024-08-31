from django.urls import path
from .views import blog
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', blog, name='blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)