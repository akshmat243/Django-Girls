from .models import Blog
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content')