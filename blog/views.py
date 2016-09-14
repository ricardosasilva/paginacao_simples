from blog.models import Post
from django.shortcuts import get_object_or_404, render


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'post': post})
