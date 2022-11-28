from django.urls import include, path
from rest_framework import routers
from django.contrib import admin

from homenagem.views import HomenagemViewSet
from .views import ActivateUserAccount, GroupViewSet

# IMPORTAR BIBLIOTECA QUE NOS RETORNA AUTH TOKEN
from rest_framework.authtoken import views


# importações para trabalhar com imagens
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
# no lugar do UserViewSet, iremos usar as urls do Djoser
# router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
# SEMPRE APÓS DEFINIR UM get_queryset TEMOS QUE DIZER SEU BASENAME
router.register(r'homenagens', HomenagemViewSet, basename='Homenagem')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    # path('auth/', include('djoser.urls.jwt')),
    # REALIZAR A ATIVAÇÃO DO USUÁRIO PELO LINK QUE O DJOSER ENVIOU NO EMAIL
    path('users/activate/<str:uidb64>/', ActivateUserAccount, name='ActivateUserAccount'),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #para caso vá trabalhar com imagens