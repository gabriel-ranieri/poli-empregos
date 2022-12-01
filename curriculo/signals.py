from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import Estudante
from .models import Curriculo

@receiver(post_save, sender=Estudante)
def create_curriculo(sender, instance, created, **kwargs):
    if created:
        Curriculo.objects.create(estudante=instance)