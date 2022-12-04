from django.db import models
from django.conf import settings
from user.models import Empresa, Estudante
from curriculo.models import Curriculo
from django.utils import timezone


class Propostas(models.Model):
    name = models.CharField(max_length=255) #name = name
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    descricao = models.TextField() #descricao = descricao
    logo_proposta = models.URLField(max_length=200) #logo_proposta = logo_proposta
    n_vagas = models.IntegerField() #numero de vagas disponíveis
    data_pub = models.DateTimeField(default=timezone.now)
    inscrito = models.ManyToManyField(Curriculo, default = None, blank = True)

    def __str__(self):
        return f'{self.name}'

# Create your models here.