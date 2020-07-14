from django.contrib import admin
from .models import Article, Tag, Commentary
# Register your models here.

# admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Commentary)

@admin.register(Article)
class article_admin(admin.ModelAdmin):
    filter_horizontal = ('tags',)