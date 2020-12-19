from django.db import models


class TestBlog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
