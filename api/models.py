from django.db import models


class Post(models.Model):
    class Meta:
        ordering = ['created']

    title = models.CharField(max_length=100, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        ordering = ['created']

    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:20]


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=100, blank=False)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='categories')
    posts = models.ManyToManyField(Post, related_name='categories', blank=True)
