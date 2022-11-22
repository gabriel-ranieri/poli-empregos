from django.db import models
from django.conf import settings


class Propostas(models.Model):
    name = models.CharField(max_length=255) #name = name
    descricao = models.TextField() #descricao = descricao
    logo_proposta = models.URLField(max_length=200, null=True) #logo_proposta = logo_proposta
    n_vagas = models.IntegerField() #numero de vagas disponíveis

    def __str__(self):
        return f'{self.name} ({self.descricao})'

# Create your models here.
