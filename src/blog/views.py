from django.shortcuts import render, get_object_or_404          # -7b : add 404

from .models import Post, Comment                              # -6a, -8d
from .forms import NewComment, PostCreateForm                  # -9b, -27f
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage  # -24a
from django.views.generic import CreateView, UpdateView, DeleteView       # -27a, 28a, 29a 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # -27g, 28d

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



class PostCreateView(LoginRequiredMixin, CreateView):        # -27a
    model = Post
    # 27f fields = ['title', 'content']
    template_name = 'blog/new_post.html'
    form_class = PostCreateForm                             # -27f

    def form_valid(self, form):                             # -27c
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):        # -28a, 28d
    model = Post
    template_name = 'blog/post_update.html'
    form_class = PostCreateForm                             

    def form_valid(self, form):                             
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):                                # -28d
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):        # -29a
    model = Post
    success_url = '/'                                                             # -29c
    
    def test_func(self):                                # -29a
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


