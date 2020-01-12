from django import forms                # -14a
from django.contrib.auth.models import User
from .models import Profile                                             # -26a

class UserCreationForm(forms.ModelForm):                                 # -14a
    username = forms.CharField(
        label='اسم المستخدم', max_length=30, help_text='اسم المستخدم يجب الا يحتوي على مسافات')     # -15a
    email = forms.EmailField(label='البريد الالكتروني')
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='الاسم الاخير')
    password1 = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(label='تاكيد كلمة المرور', widget=forms.PasswordInput(), min_length=8)
    class Meta:                                                         # -14a
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_password2(self):                                          # -15a
        cd = self.cleaned_data      # cd = clean data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('كلمة المرور غير متطابقة')
        return cd['password2']

    def clean_username(self):                                           # -15a
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('يوجد مستخدم  بهذا الاسم')
        return cd['username']


class LoginForm(forms.ModelForm):                                       # -17a
    username = forms.CharField(label='اسم المستخدم')                   # -17d
    password = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput())
    class Meta:                                                         # -17a
        model = User
        fields = ('username', 'password')


class UserUpdateForm(forms.ModelForm):                                 # -26a
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='الاسم الاخير')
    email = forms.EmailField(label='البريد الالكتروني')
    class Meta:                                                         # -26a
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileUpdateForm(forms.ModelForm):                               # -26a
    class Meta:
        model = Profile
        fields = ('image',)
