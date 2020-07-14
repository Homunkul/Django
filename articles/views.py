from django.shortcuts import render
from .models import Article
# Create your views here.

def articles_overview(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles_overview.html', context)

def get_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'article.html', {'article': article})