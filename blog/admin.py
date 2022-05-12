from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at', 'created_at', 'status')
    ordering = ('-published_at', 'status')
    list_filter = ('title', 'author', 'published_at', 'status')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Article, ArticleAdmin)
