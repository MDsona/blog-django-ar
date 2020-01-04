from django.shortcuts import render

from .forms import UserCreationForm                     # -14b

# Create your views here.

def register(request):                                  # -14b
    form = UserCreationForm()

    return render(request, 'user/register.html', {
        'page_title': 'تسجيل جديد',
        'form': form,
    })
