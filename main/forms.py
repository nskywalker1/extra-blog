import mimetypes

from django import forms
from django.core.exceptions import ValidationError

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'preview_image', 'video', 'category', 'tags']
