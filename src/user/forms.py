from django import forms                # -14a
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):      # -14a
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
