from django import forms                # -9a
from .models import Comment, Post       # -9a, 27e             

class NewComment(forms.ModelForm):      # -9a
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', )


class PostCreateForm(forms.ModelForm):                                  # -27e
    title = forms.CharField(label='عنوان التدوينة')
    content = forms.CharField(label='نص التدوينة', widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ('title', 'content')
