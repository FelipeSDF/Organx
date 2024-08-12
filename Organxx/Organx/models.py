from django.db import models
from django.utils import timezone

class Cadastrados(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    unidade = models.CharField(max_length=100, null=True, blank=True)
    cargo = models.CharField(max_length=100,null=True, blank=True)
    empresa = models.CharField(max_length=100,null=True, blank=True)
    Função = models.CharField(max_length=100,null=True, blank=True)
    data_add = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.nome