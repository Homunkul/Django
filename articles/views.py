from django.shortcuts import render
from .models import Article, Tag, Commentary
from rest_framework import viewsets,filters
from .serializevs import ArticleSerializer, TagSerializer, CommentarySerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def articles_overview(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles_overview.html', context)

def get_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'article.html', {'article': article})

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    search_fields = ['name', 'description', 'content', 'author__id', 'tags__name', 'commentaries__content']
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CommentaryViewSet(viewsets.ModelViewSet):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


