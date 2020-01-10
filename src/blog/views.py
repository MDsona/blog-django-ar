from django.shortcuts import render, get_object_or_404          # -7b : add 404

from .models import Post, Comment                              # -6a, -8d
from .forms import NewComment                                   # -9b
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage  # - 24a

# Create your views here.

# -6a posts = [                                                         # -3a
#     {
#         'title': 'التدوينة الاولى',
#         'content': 'نص التدوينة نـــصــ تـجريبيـــ',
#         'post_date': '15-12-2019',
#         'author': 'MDsona'
#     },
#     {
#         'title': 'التدوينة الاولى',
#         'content': 'نص التدوينة نـــصــ تـجريبيـــ',
#         'post_date': '15-12-2019',
#         'author': 'olom web'
#     },
#     {
#         'title': 'التدوينة الاولى',
#         'content': 'نص التدوينة نـــصــ تـجريبيـــ',
#         'post_date': '15-12-2019',
#         'author': 'olom web'
#     }
# ]

def home(request):                                                  # -2b {'title': 'home'}
    posts = Post.objects.all()                                      # -24a
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:                                                            # -24a
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_page)

    context = {                                                     # -3a
        'page_title': 'الصفحة الرئيسية',
        'posts': posts,                                              # -6a, 24a
        'page': page,                                               # -24b
    }
    return render(request, 'blog/index.html', context)


def about(request):                                                 # -4a
    context = {
        'page_title': 'من أنا'
    }

    return render(request, 'blog/about.html', context)                       # -4a


def post_detail(request, post_id):                          # -7a
    post = get_object_or_404(Post, pk=post_id)               # -7b
    comments = post.comments.filter(active=True)           # -8d   post.related_name
    # >< comment_form = NewComment()                             # -9b
    # >< new_comment = None                                      # -11b
    
    # check before save data from comment form
    if request.method == 'POST':                            # -11a
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():                         # -11b
            new_comment = comment_form.save(commit=False)
            new_comment.post = post                         # الارتباط بجدول التدوينات
            new_comment.save()
            comment_form = NewComment()
    else:
        comment_form = NewComment
    
    context = {
        'page_title': post,
        'post': post,                                       # -7b
        'comments': comments,                              # -8d
        'comment_form': comment_form,                       # -9b
    }

    return render(request, 'blog/detail.html', context)





