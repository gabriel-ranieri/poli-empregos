from django.contrib import admin
from .models import User, Estudante, Empresa
# Register your models here.
admin.site.register(User)
admin.site.register(Empresa)
admin.site.register(Estudante)