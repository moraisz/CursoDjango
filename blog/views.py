from django.http import HttpRequest
from django.shortcuts import render

from blog.data import posts


def blog(request):
    context = {
        'title': 'Blog',
        'text2': 'BLOG',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context,
    )


def post(request: HttpRequest, post_id: int):
    found_post = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    context = {
        'title': 'Posts',
        'posts': [found_post]
    }

    return render(
        request,
        'blog/index.html',
        context,
    )


def exemplo(request):
    context = {
        'title': 'Exemplo',
        'text2': 'EXEMPLO',
    }

    return render(request,
                  'blog/exemplo.html',
                  context,
                  )
