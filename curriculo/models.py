from django.db import models
from django.conf import settings
from user.models import Estudante

class Curso(models.Model):
    descricao = models.CharField(max_length=255,null=True)

    def __str__(self):
        return f'"{self.descricao}"'

class Curriculo(models.Model):
    estudante = models.OneToOneField(Estudante,on_delete=models.CASCADE)
    curso = models.OneToOneField(Curso,on_delete=models.CASCADE,null=True)
    bio = models.TextField(null=True)
    foto = models.URLField(max_length=200, null=True)
    profissional = models.TextField(null=True)
    academico = models.TextField(null=True)
    experiencia = models.TextField(null=True)

    def __str__(self):
        return f'"{self.estudante}"'

