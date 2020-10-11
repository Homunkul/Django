from rest_framework import serializers
from .models import Article, Tag, Commentary


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'name', 'description', 'content', 'author', 'creation_time', 'commentaries')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = ('id', 'content', 'articles', 'author', 'creation_time')
