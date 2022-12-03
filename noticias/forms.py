from django.forms import ModelForm
from .models import Noticia, Comment


class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = [
            'name',
            'descricao',
            'poster_url',
        ]
        labels = {
            'name': 'Título da notícia',
            'descricao': 'Descrição',
            'poster_url': 'URL da imagem',
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]
        labels = {
            'text': 'Comentário',
        }