from django.shortcuts import render, redirect                   # , re

from .forms import UserCreationForm, LoginForm                  # -14b, 17b
from django.contrib import messages                             # -15b
from django.contrib.auth import authenticate, login, logout     # -17e
from blog.models import Post                                    # -19a
from django.contrib.auth.decorators import login_required       # -22a
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage  # - 25a

# Create your views here.

def register(request):                                          # -14b
    # 15b form = UserCreationForm()
    if request.method == 'POST':                                # -15b
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # 15c form.save()
            new_user = form.save(commit=False)                 # -15c
            # 15c username = form.cleaned_data['username']
            new_user.set_password(form.cleaned_data['password1'])   # -15c
            new_user.save()                                         # -15c
            messages.success(request, f'تهانينا {new_user} لقد تمت عملية التسجيل بنجاح') # 15c {username}
            return redirect('login_url')            # go to index.html, 

    else:
        form = UserCreationForm()

    return render(request, 'user/register.html', {              # -14b
        'page_title': 'تسجيل جديد',
        'form': form,
    })


def login_user(request):                                        # -17b
    if request.method == 'POST':                                # -17e
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile_url')                       # home_url
        else:
            messages.warning(request, 'خطأ في اسم المستخدم او كلمة المرور')
    
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {                 # -17b
        'page_title': 'تسجيل الدخول',
        'form': form
    })


def logout_user(request):                                       # -17f
    logout(request)
    return render(request, 'user/logout.html', {
        'page_title': 'تسجيل الخروج',
    })


@login_required(login_url='login_url')                          # -22a
def profile(request):                                           # -18a
    posts = Post.objects.filter(author=request.user)            # -19a
    post_list = Post.objects.filter(author=request.user)        # -25a
    paginator = Paginator(post_list, 5)                             # -25a
    page = request.GET.get('page')
    try:                                                        # -25a
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_page)
    return render(request, 'user/profile.html', {
        'page_title': 'الملف الشخصي',
        'posts': posts,
        'page': page,                                            # -25a
        'post_list': post_list,
    })

