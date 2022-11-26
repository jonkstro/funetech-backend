from rest_framework import viewsets
from rest_framework import permissions, authentication

from .models import Homenagem
from .serializers import HomenagemSerializer


class HomenagemViewSet(viewsets.ModelViewSet):
    serializer_class = HomenagemSerializer

    # CONFIGURAR PARA SÓ EXIBIR SE ESTIVER AUTENTICADO COM TOKEN
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [
            authentication.TokenAuthentication, 
            authentication.SessionAuthentication
        ]
    # SERÁ MOSTRADO SOMENTE AS LISTAS DO USUÁRIO QUE TIVER LOGADO
    def get_queryset(self):
        user = self.request.user
        return Homenagem.objects.filter(user=user)