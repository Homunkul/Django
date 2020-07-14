from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_overview),
    path('article/<uuid:article_id>', views.get_article),
]