from django import forms
from .models import Curso, Curriculo
from user.models import User, Estudante

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']

class CurriculoForm(forms.Form):
    curso = forms.ModelChoiceField(queryset = Curso.objects.all())
    bio = forms.CharField(widget=forms.Textarea())
    foto = forms.URLField(max_length=200)
    profissional = forms.CharField(widget=forms.Textarea())
    academico = forms.CharField(widget=forms.Textarea())
    experiencia = forms.CharField(widget=forms.Textarea())
    #class Meta:
        #model = Curriculo
        #fields = [
         #   'bio',
         #   'foto',
         #   'profissional',
          #   'experiencia',
       # ]
        #labels = {
        #    'bio':'BIO',
       #     'foto':'URL da Foto',
       #     'profissional':'Profissional',
      #      'academico':'Acadêmico',
       #     'experiencia':'Experiência',
       # }

class CursoForm(forms.Form):
    class Meta:
        model = Curso
        fields = [
            'descricao',
        ]
        labels = {
            'descricao':'Curso',
        }