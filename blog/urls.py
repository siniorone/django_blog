from django.urls import path
from .views import HomeBlogView, ArticleDetailView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'
urlpatterns = [
    path('blog/', HomeBlogView.as_view(), name="blog_home"),
    path('blog/<slug:slug>/', ArticleDetailView.as_view(), name="article_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
