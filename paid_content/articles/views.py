from django.shortcuts import render
from .models import Article, User

def show_articles(request):
    context = {}

    if request.user.has_subscription:
        context['articles'] = Article.objects.only('id', 'title')
    else:
        context['articles'] = Article.objects.filter(premium=False).only('id', 'title')

    return render(
        request,
        'articles.html',
        context
    )


def show_article(request, id):
    context = {}

    context['article'] = Article.objects.get(id = id)

    return render(
        request,
        'article.html',
        context
    )
