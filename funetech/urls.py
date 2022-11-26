from django.urls import include, path
from rest_framework import routers
from django.contrib import admin

from homenagem.views import HomenagemViewSet
from .views import UserViewSet, GroupViewSet

# IMPORTAR BIBLIOTECA QUE NOS RETORNA AUTH TOKEN
from rest_framework.authtoken import views


# importações para trabalhar com imagens
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
# SEMPRE APÓS DEFINIR UM get_queryset TEMOS QUE DIZER SEU BASENAME
router.register(r'homenagens', HomenagemViewSet, basename='Homenagem')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #para caso vá trabalhar com imagens