from django import forms
from blog.models import  Post


class PostForm (forms.Form):
    title=forms.CharField(max_length=100)