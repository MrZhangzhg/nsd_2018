from django.shortcuts import render
from .models import Article

def index(request):
    articles = Article.objects.order_by('-pub_date')
    return render(request, 'blog_index.html', {'articles': articles})
