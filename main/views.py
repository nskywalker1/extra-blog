from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
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
    post = get_object_or_404(Post, slug=post_slug)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('main:post_detail', post_slug=post_slug)
    else:
        form = CommentForm()
    return render(request, 'main/detail.html', {"post": post, 'comments': comments, "form": form})
