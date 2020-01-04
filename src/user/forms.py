from django import forms                # -14a
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):                                 # -14a
    username = forms.CharField(label='اسم المستخدم', max_length=30)     # -15a
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
