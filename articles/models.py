from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='articles')
    tags = models.ManyToManyField('Tag', related_name='articles')
    Creation_time = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Commentary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    articles = models.ForeignKey(Article, related_name='commentaries', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='commentaries', on_delete=models.CASCADE)
    Creation_time = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        if len(self.content)<30:
            return self.content
        return self.content[:30]+'/...'

    class Meta:
        verbose_name_plural = 'commentaries'