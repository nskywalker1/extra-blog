from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.published_posts()
    return render(request, 'main/list.html', {'posts': posts})
