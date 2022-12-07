from django.db import models
from django.contrib.auth.models import User


class Homenagem(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=50, null=False, blank=False)
    data_nasc = models.DateField(null=False, blank=False)
    cidade_nasc = models.CharField(max_length=50, null=False, blank=False)
    data_falec = models.DateField(null=False, blank=False)
    cidade_falec = models.CharField(max_length=50, null=False, blank=False)
    memoria = models.TextField(max_length=255, null=True, blank=True)
    biografia = models.TextField(max_length=800, null=True, blank=True)
    foto = models.ImageField(upload_to='homenagem', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
