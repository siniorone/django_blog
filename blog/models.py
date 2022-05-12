from django.db import models
from django.conf import settings
from django.utils import timezone


def thumbnail_upload_to(instance, filename):
    return f"images/users/{instance.author}/{filename}"


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to=thumbnail_upload_to, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, choices=(('d', 'Draft'), ('p', 'Published')))

    def __str__(self):
        return f"{self.author} | {self.title}"
