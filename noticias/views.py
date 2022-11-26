from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .temp_data import noticia_data
from django.shortcuts import render, get_object_or_404
from .models import Noticia
from django.urls import reverse

def detail_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    context = {'noticia': noticia}
    return render(request, 'noticias/detail.html', context)

def list_noticias(request):
    noticia_list = Noticia.objects.all()
    context = {'noticia_list': noticia_list}
    return render(request, 'noticias/index.html', context)

def search_noticias(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        noticia_list = Noticia.objects.filter(name__icontains=search_term)
        context = {"noticia_list": noticia_list}
    return render(request, 'noticias/search.html', context)

def create_noticia(request):
    if request.method == 'POST':
        noticia_name = request.POST['name']
        noticia_poster_url = request.POST['poster_url']
        noticia = Noticia(name=noticia_name,
                      poster_url=noticia_poster_url)
        noticia.save()
        return HttpResponseRedirect(
            reverse('noticias:detail', args=(noticia.id, )))
    else:
        return render(request, 'noticias/create.html', {})

def update_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)

    if request.method == "POST":
        noticia.name = request.POST['name']
        noticia_poster_url = request.POST['poster_url']
        noticia.save()
        return HttpResponseRedirect(
            reverse('noticias:detail', args=(noticia.id, )))

    context = {'noticia': noticia}
    return render(request, 'noticias/update.html', context)


def delete_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)

    if request.method == "POST":
        noticia.delete()
        return HttpResponseRedirect(reverse('noticias:index'))

    context = {'noticia': noticia}
    return render(request, 'noticias/delete.html', context)