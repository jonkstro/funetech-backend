from django.http import HttpResponse, HttpResponseRedirect
import base64
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import UserSerializer, GroupSerializer

# Realizar autenticação pelo email do Djoser
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK, 
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT
    )
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]
    

# ATIVAR O USUÁRIO ATRAVÉS DO LINK QUE O DJOSER ENVIOU NO EMAIL
def ActivateUserAccount(request, uidb64=None):
    try:
        # UID DO DJOSER VEM EM BASE64, SERÁ PRECISO DECODIFICAR
        uid = base64.b64decode(uidb64 + (b'==').decode('utf-8'))
        # FAZER A BUSCA DO USUÁRIO PELO ID DO DJOSER DECODIFICADO
        user = User.objects.get(pk=uid)
    
    # CASO O USUÁRIO NÃO EXISTA:
    except User.DoesNotExist:
        user = None

    # CASO USUÁRIO EXISTA:
    if user:
        user.is_email_verified = True
        user.is_active = True
        user.save()
        return HttpResponse("Conta ativada",status=HTTP_200_OK) 
    else:
        return HttpResponse("Falha ao tentar ativar a conta",status=HTTP_400_BAD_REQUEST) 
         
