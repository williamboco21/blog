from django.shortcuts import render

# from the current package from the root, import the class
from .models import Post

# Create your views here.


def home_view(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)


def about_view(request):
    return render(request, 'blog/about.html', {'title': 'About'})