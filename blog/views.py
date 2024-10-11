from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import render, redirect

from blog.models import Post


def index(request):
    return redirect(reverse('posts_list'))


def posts_list(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(Post.objects.all(), 10)
    page = paginator.get_page(page_number)
    context = {
        'posts_list': page,
        'page': page
    }
    return render(request, 'blog/index.html', context)
