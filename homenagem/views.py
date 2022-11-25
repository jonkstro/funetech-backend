from rest_framework import viewsets
from rest_framework import permissions

from .models import Homenagem
from .serializers import HomenagemSerializer


class HomenagemViewSet(viewsets.ModelViewSet):
    queryset = Homenagem.objects.all()
    serializer_class = HomenagemSerializer
    permission_classes = [permissions.IsAuthenticated]