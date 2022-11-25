from django.urls import include, path
from rest_framework import routers
from django.contrib import admin

from homenagem.views import HomenagemViewSet
from .views import UserViewSet, GroupViewSet

# importações para trabalhar com imagens
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'homenagens', HomenagemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #para caso vá trabalhar com imagens