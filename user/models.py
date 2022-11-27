from django.db import models
from django.contrib.auth.models import User
from django_cpf_cnpj.fields import CPFField, CNPJField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_estudante=models.BooleanField(default=False)
    is_empresa=models.BooleanField(default=False)

class Estudante(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=2)

    def __str__(self):
        return self.user.username
    
class Empresa(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
