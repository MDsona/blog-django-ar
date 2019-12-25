from django.shortcuts import render

# Create your views here.

posts = [                                                         # -3a
    {
        'title': 'التدوينة الاولى',
        'content': 'نص التدوينة نـــصــ تـجريبيـــ',
        'post_date': '15-12-2019',
        'author': 'MDsona'
    },
    {
        'title': 'التدوينة الاولى',
        'content': 'نص التدوينة نـــصــ تـجريبيـــ',
        'post_date': '15-12-2019',
        'author': 'olom web'
    },
    {
        'title': 'التدوينة الاولى',
        'content': 'نص التدوينة نـــصــ تـجريبيـــ',
        'post_date': '15-12-2019',
        'author': 'olom web'
    }
]

def home(request):                                                  # -2b {'title': 'home'}
    context = {                                                     # -3a
        'page_title': 'الصفحة الرئيسية',
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def about(request):                                                 # -4a
    context = {
        'page_title': 'من أنا'
    }

    return render(request, 'blog/about.html', context)                       # -4a





