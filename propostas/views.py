from django.shortcuts import render
from django.http import HttpResponse
from .temp_data import propostas_data
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Propostas
from django.contrib.auth.decorators import login_required, permission_required

from user.models import User, Estudante

@login_required
def detail_propostas(request, propostas_id):
    propostas = get_object_or_404(Propostas, pk=propostas_id)
    context = {'propostas': propostas}
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
@permission_required('propostas.create_propostas')
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
# Create your views here.
