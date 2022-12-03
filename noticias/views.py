from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .temp_data import noticia_data
from django.shortcuts import render, get_object_or_404
from .models import Noticia
from django.urls import reverse
from .models import Noticia, Comment
from .forms import NoticiaForm, CommentForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def detail_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    context = {'noticia': noticia}
    return render(request, 'noticias/detail.html', context)

@login_required
def list_noticias(request):
    noticia_list = Noticia.objects.all()
    context = {'noticia_list': noticia_list}
    return render(request, 'noticias/index.html', context)

@login_required
def search_noticias(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        noticia_list = Noticia.objects.filter(name__icontains=search_term)
        context = {"noticia_list": noticia_list}
    return render(request, 'noticias/search.html', context)

@login_required
@permission_required('noticia.create_noticia')
def create_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            noticia_name = form.cleaned_data['name']
            noticia_descricao = form.cleaned_data['descricao']
            noticia_poster_url = form.cleaned_data['poster_url']
            noticia = Noticia(name=noticia_name,
                          descricao=noticia_descricao,
                          poster_url=noticia_poster_url)
            noticia.save()
            return HttpResponseRedirect(
                reverse('noticias:detail', args=(noticia.id, )))
    else:
        form = NoticiaForm()
    context = {'form': form}
    return render(request, 'noticias/create.html', context)

@login_required
@permission_required('noticia.change_noticia')
def update_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)

    if request.method == "POST":
        form = NoticiaForm(request.POST)
        if form.is_valid():
            noticia.name = form.cleaned_data['name']
            noticia.descricao = form.cleaned_data['descricao']
            noticia.poster_url = form.cleaned_data['poster_url']
            noticia.save()
            return HttpResponseRedirect(
                reverse('noticias:detail', args=(noticia.id, )))
    else:
        form = NoticiaForm(
            initial={
                'name': noticia.name,
                'descricao': noticia.descricao,
                'poster_url': noticia.poster_url
            })

    context = {'noticia': noticia, 'form': form}
    return render(request, 'noticias/update.html', context)

@login_required
@permission_required('noticia.delete_noticia')
def delete_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)

    if request.method == "POST":
        noticia.delete()
        return HttpResponseRedirect(reverse('noticias:index'))

    context = {'noticia': noticia}
    return render(request, 'noticias/delete.html', context)

@login_required
def create_comment(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = request.user
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            noticia = noticia)
            comment.save()
            return HttpResponseRedirect(
                reverse('noticias:detail', args=(noticia_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'noticia': noticia}
    return render(request, 'noticias/comment.html', context)