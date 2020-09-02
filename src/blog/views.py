from django.shortcuts import render
from django.views.generic import ListView

# from the current package from the root, import the class
from .models import Post

# Create your views here.


# def home_view(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/index.html', context)


class PostsListView(ListView):
    model = Post
    template_name = 'blog/index.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


def about_view(request):
    return render(request, 'blog/about.html', {'title': 'About'})