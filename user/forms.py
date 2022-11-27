from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Estudante, Empresa, User
from django_cpf_cnpj.fields import CPFField, CNPJField
from django.contrib.auth.models import Group

class EstudanteSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name=forms.CharField(required=True)
    cpf=forms.CharField(required=True)
    

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_estudante = True
        user.save()

        user_group = Group.objects.get(name='Estudantes')
        user.groups.add(user_group)
        estudante = Estudante.objects.create(user=user)
        estudante.name=self.cleaned_data.get('name')
        estudante.cpf=self.cleaned_data.get('cpf')
        user.save()
        estudante.save()

        return estudante

class EmpresaSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name=forms.CharField(required=True)
    cnpj=forms.CharField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User
 
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_empresa = True
        user.save()
        
        user_group = Group.objects.get(name='Empresas')
        user.groups.add(user_group)
        empresa = Empresa.objects.create(user=user)
        empresa.name=self.cleaned_data.get('name')
        empresa.cnpj=self.cleaned_data.get('cnpj')
        user.save()
        empresa.save()
 
        return empresa