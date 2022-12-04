from django.shortcuts import render
from django.http import HttpResponse
from .temp_data import propostas_data
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Propostas
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied


from user.models import User, Estudante
from curriculo.models import Curriculo

@login_required
def detail_propostas(request, propostas_id):
    propostas = get_object_or_404(Propostas, pk=propostas_id)
    ins = bool
    context = {'propostas': propostas, 'ins': ins}
    if request.user.is_estudante:
        curriculo = request.user.estudante.curriculo
        if propostas.inscrito.filter(id = request.user.estudante.curriculo.id).exists():
            ins = True
        context = {'propostas': propostas, 'ins': ins, 'curriculo':curriculo}
    return render(request, 'propostas/detail.html', context)

@login_required
def get_empresa_profile(request,username):
    user = User.objects.get(username=username)
    propostas_list = Propostas.objects.filter(empresa=user.empresa)
    #propostas_list = Propostas.objects.get(empresa=user.empresa)
    return render(request, 'propostas/empresa_profile.html', {"user":user, 'propostas_list': propostas_list})

@login_required
def list_propostas(request):
    propostas_list = Propostas.objects.all()
    context = {'propostas_list': propostas_list}
    return render(request, 'propostas/index.html', context)

@login_required
def search_propostas(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        propostas_list = Propostas.objects.filter(name__icontains=search_term)
        context = {"propostas_list": propostas_list}
    return render(request, 'propostas/search.html', context)

@login_required
@permission_required('propostas.add_propostas')
def create_propostas(request):
    if request.method == 'POST':
        propostas_name = request.POST['name']
        propostas_empresa = request.user.empresa
        propostas_descricao = request.POST['descricao']
        propostas_logo_proposta = request.POST['logo_proposta']
        propostas_n_vagas = request.POST['n_vagas']
        #propostas_data_pub = request.POST['data_pub']
        propostas = Propostas(name=propostas_name,
                       empresa = propostas_empresa,
                      descricao=propostas_descricao,
                      logo_proposta=propostas_logo_proposta,
                      n_vagas=propostas_n_vagas)#,
                      #data_pub=propostas_data_pub)
        propostas.save()
        return HttpResponseRedirect(
            reverse('propostas:detail', args=(propostas.id, )))
    else:
        return render(request, 'propostas/create.html', {})

@login_required
@permission_required('propostas.change_propostas')
def update_propostas(request, propostas_id):
    propostas = get_object_or_404(Propostas, pk=propostas_id)

    if not (propostas.empresa == request.user.empresa or request.user.is_superuser):
        raise PermissionDenied

    if request.method == "POST":
        propostas.name = request.POST['name']
        propostas_empresa = request.user.empresa
        propostas.descricao = request.POST['descricao']
        propostas_logo_proposta = request.POST['logo_proposta']
        propostas_n_vagas = request.POST['n_vagas']
        propostas.save()
        return HttpResponseRedirect(
            reverse('propostas:detail', args=(propostas.id, )))

    context = {'propostas': propostas}
    return render(request, 'propostas/update.html', context)

@login_required
@permission_required('propostas.delete_propostas')
def delete_propostas(request, propostas_id):
    propostas = get_object_or_404(Propostas, pk=propostas_id)

    if request.method == "POST":
        propostas.delete()
        return HttpResponseRedirect(reverse('propostas:index'))

    context = {'propostas': propostas}
    return render(request, 'propostas/delete.html', context)

def inscrito_add(request, id):
    propostas = get_object_or_404(Propostas, id = id)
    if request.user.is_estudante:
        if propostas.inscrito.filter(id = request.user.estudante.curriculo.id).exists():
            propostas.inscrito.remove(request.user.estudante.curriculo)

        else:
            propostas.inscrito.add(request.user.estudante.curriculo)


    return HttpResponseRedirect(reverse('propostas:index'))

def inscrito_list(request,propostas_id):
    propostas = get_object_or_404(Propostas, id = propostas_id)

    if request.user.is_estudante:
        raise PermissionDenied
    else:
        if not (request.user.is_superuser):
            if not (propostas.empresa == request.user.empresa):
                raise PermissionDenied

    i_list = Curriculo.objects.filter(propostas = propostas_id)
    context = {'propostas': propostas, 'i_list' : i_list}
    return render(request, 'propostas/inscrito_list.html', context)


def propostas_inscrito_list(request,username):
    user = User.objects.get(username=username)

    if request.user.is_empresa:
        raise PermissionDenied

    curriculo = Curriculo.objects.get(estudante=user.estudante) 

    p_list = Propostas.objects.filter(inscrito = curriculo.id)
    context = {'user':user, 'curriculo': curriculo, 'p_list' : p_list}
    return render(request, 'propostas/inscricoes.html', context)
# Create your views here.

#class InscritoCreateView(generic.CreateView):
   # model = Inscrito
   # template_name = 'propostas/create_inscrito.html'
    #success_url = reverse_lazy('propostas:inscritos')