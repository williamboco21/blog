from django.shortcuts import render

posts = [
    {
        'author': 'William',
        'title': 'Blog Post 1',
        'content': 'This is my first post content',
        'date_posted': 'September 1, 2020'
    },
    {
        'author': 'django',
        'title': 'Blog Post 2',
        'content': 'This is my second post content',
        'date_posted': 'August 31, 2020'
    },
]

# Create your views here.


def home_view(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def about_view(request):
    return render(request, 'blog/about.html', {'title': 'About'})