from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class PostManager(models.Manager):
    def published_posts(self):
        return self.filter(is_published=True)


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/%Y/%m/%d', blank=True)
    preview_image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts_by_category')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts_by_tags')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    objects = PostManager()

    def get_absolute_url(self):
        return reverse('login:post_detail', kwargs={'post_slug': self.slug})

    def total_comments(self):
        return self.comments.count()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        indexes = [models.Index(fields=['title'])]
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}: {self.content}'
