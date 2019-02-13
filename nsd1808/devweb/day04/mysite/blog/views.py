from django.shortcuts import render
from .models import Article

def index(request):
    articles = Article.objects.order_by('-pub_date')
    return render(request, 'blog_index.html', {'articles': articles})

def show_article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'show_article.html', {'article': article})
