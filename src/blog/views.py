from django.shortcuts import render

# Create your views here.

def home(request):                                                  # -2b
    return render(request, 'blog/index.html', {'title': 'home'})

