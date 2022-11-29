from django.urls import include, path
from rest_framework import routers
from django.contrib import admin

from homenagem.views import HomenagemViewSet


# importações para trabalhar com imagens
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
# SEMPRE APÓS DEFINIR UM get_queryset TEMOS QUE DIZER SEU BASENAME
router.register(r'homenagens', HomenagemViewSet, basename='Homenagem')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken')),
    # path('auth/', include('djoser.social.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #para caso vá trabalhar com imagens