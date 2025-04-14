from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.published_posts()
    search_query = request.GET.get('query')

    if search_query:
        posts = posts.filter(title__icontains=search_query)

    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/list.html', {"posts": page_obj, "search_query": search_query})


def post_detail(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    return render(request, 'main/detail.html', {"post": post})
