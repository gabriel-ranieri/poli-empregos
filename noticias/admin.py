from django.contrib import admin

from .models import Noticia, Comment

admin.site.register(Noticia)
admin.site.register(Comment)