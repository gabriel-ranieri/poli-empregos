from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
import requests
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Curso, Curriculo
from .forms import CursoForm, CurriculoForm
from user.models import User, Estudante

# CURRICULO #
@login_required
def curriculo_detail(request, curriculo_id):
    #estudante = get_object_or_404(Estudante, pk=estudante_id)
    curriculo = get_object_or_404(Curriculo, pk=curriculo_id)
    context = {'curriculo': curriculo}
    #curriculo_detail = get_object_or_404(Curriculo, estudante=estudante)
    return render(request, 'curriculo/profile.html', context)  #,'estudante': estudante})

class CurriculoListView(generic.ListView):
    model = Curriculo
    template_name = 'curriculo/list.html'

def search_curriculo(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query']
        curriculo_list = Curriculo.objects.filter(estudante__name__icontains=search_term)
        context = {"curriculo_list": curriculo_list}

    return render(request, 'curriculo/search.html', context)

@permission_required('curriculo.change_curriculo')
def update_curriculo(request, curriculo_id):
    curriculo = get_object_or_404(Curriculo, pk=curriculo_id)

    if request.method == "POST":

        form = CurriculoForm(request.POST)

        if form.is_valid():
            curriculo.curso = form.cleaned_data['curso']
            curriculo.bio = form.cleaned_data['bio']
            curriculo.foto = form.cleaned_data['foto']
            curriculo.profissional = form.cleaned_data['profissional']
            curriculo.academico = form.cleaned_data['academico']
            curriculo.experiencia = form.cleaned_data['experiencia']
            curriculo.save()
            return HttpResponseRedirect(
                reverse('curriculo:profile', args=(curriculo.id, )))

    else:
        form = CurriculoForm(
            initial={
                'curso': curriculo.curso,
                'bio': curriculo.bio,
                'foto': curriculo.foto,
                'profissional': curriculo.profissional,
                'academico': curriculo.academico,
                'experiencia': curriculo.experiencia
            })

    context = {'curriculo': curriculo, 'form': form}
    return render(request, 'curriculo/update.html', context)

# CURSO #