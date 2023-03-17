from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from posts.models import Group, Post


def index(request):
    posts = Post.objects.all()
    template = 'posts/index.html'
    context = {'posts': posts}
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    template = 'posts/group_list.html'
    context = {'group': group, 'posts': posts}
    return render(request, template, context)
