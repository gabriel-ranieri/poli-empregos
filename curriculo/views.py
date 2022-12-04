from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied

from .models import Curso, Curriculo
from .forms import CursoForm, CurriculoForm
from user.models import User, Estudante

# CURRICULO #
@login_required
def curriculo_detail(request, curriculo_id):
    #estudante = request.user.estudante
   curriculo = get_object_or_404(Curriculo, pk=curriculo_id)
   context = {'curriculo': curriculo}
    #curriculo_detail = get_object_or_404(Curriculo, estudante=estudante)
   return render(request, 'curriculo/profile.html', context)  #,'estudante': estudante})

@login_required
def get_user_profile(request,username):
    user = User.objects.get(username=username)
    curriculo = Curriculo.objects.get(estudante=user.estudante) 
    return render(request, 'curriculo/user_profile.html', {"user":user, 'curriculo': curriculo})

class CurriculoListView(generic.ListView,LoginRequiredMixin):
    model = Curriculo
    template_name = 'curriculo/list.html'

@login_required
def search_curriculo(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query']
        curriculo_list = Curriculo.objects.filter(estudante__name__icontains=search_term)
        context = {"curriculo_list": curriculo_list}

    return render(request, 'curriculo/search.html', context)

@login_required
@permission_required('curriculo.change_curriculo')
def update_curriculo(request, curriculo_id):

    curriculo = get_object_or_404(Curriculo, pk=curriculo_id)
    #Restringir edição ao dono do curriculo.
    if not (curriculo.estudante == request.user.estudante or request.user.is_superuser):
        raise PermissionDenied

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