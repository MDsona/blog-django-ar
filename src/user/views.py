from django.shortcuts import render, redirect           # , re

from .forms import UserCreationForm                     # -14b
from django.contrib import messages                     # -15b

# Create your views here.

def register(request):                                  # -14b
    # 15b form = UserCreationForm()
    if request.method == 'POST':                        # -15b
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'تهانينا {username} لقد تمت عملية التسجيل بنجاح')
            return redirect('home_url')            # go to index.html

    else:
        form = UserCreationForm()

    return render(request, 'user/register.html', {      # -14b
        'page_title': 'تسجيل جديد',
        'form': form,
    })
