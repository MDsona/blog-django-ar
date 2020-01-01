from django import forms                # -9a
from .models import Comment             

class NewComment(forms.ModelForm):      # -9a
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', )
