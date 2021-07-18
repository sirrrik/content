from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url
from django.urls.conf import include
from rest_framework import routers, views
from content_api.views import ItemViewSet


router = routers.DefaultRouter()
router.register(r'Item', ItemViewSet, basename='Item')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
