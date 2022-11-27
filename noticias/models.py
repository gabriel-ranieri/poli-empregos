from django.db import models
from django.conf import settings
from django.utils import timezone


class Noticia(models.Model):
    name = models.CharField(max_length=255)
    release_date  = models.DateTimeField(default=timezone.now)
    descricao = models.TextField()
    poster_url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f'{self.name} ({self.release_date})'

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'