from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import Article


# Create your views here.
class HomeBlogView(ListView):
    template_name = 'home_blog.html'
    model = Article
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'
    model = Article
    context_object_name = 'article'
