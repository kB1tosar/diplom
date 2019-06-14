from django.shortcuts import render, get_object_or_404, redirect
from .forms import ArticleForm, MapForm
from django.http import HttpResponseRedirect
from .models import Article, Map
from django.urls import reverse
from sourcecode import tiling


def index(request):
    article_list = Article.objects.all()
    map_list = Map.objects.all()
    context = {'article_list': article_list, 'map_list': map_list}
    return render(request, 'htmlpages/homepage.html', context)

def feature(request):
    return render(request, 'htmlpages/create_object_on_map.html')

def create_article(request):
    if request.method == "POST":
        form_article = ArticleForm(request.POST, request.FILES)
        if form_article.is_valid():
            article = form_article.save(commit=False)
            article.save()
            return HttpResponseRedirect(reverse('sourcecode:index'))
    else:
        form_article = ArticleForm()
    context = {'form_article': form_article}
    return render(request, 'htmlpages/new_article.html', context)


def create_map(request):
    if request.method == "POST":
        form_map = MapForm(request.POST, request.FILES)
        if form_map.is_valid():
            map_objects = form_map.save(commit=False)
            tiling.tile_work(map_objects.map_image, map_objects.map_name)
            map_objects.save()
            return HttpResponseRedirect(reverse('sourcecode:index'))
    else:
        form_map = MapForm()
    context = {'form_article': form_map}
    return render(request, 'htmlpages/new_map.html', context)


def full_description(request, pk):
    full_article = get_object_or_404(Article, pk=pk)
    context = {'full_article': full_article}
    return render(request, 'htmlpages/full_article_descripion.html', context)


def article_remove(request, pk):
    post = get_object_or_404(Article, pk=pk)
    post.delete()
    return redirect('sourcecode:index')


def article_edit(request, pk):
    post = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('sourcecode:full_description', pk=post.pk)
    else:
        form = ArticleForm(instance=post)
    context={'form': form, }
    return render(request, 'htmlpages/edit_article.html', context)