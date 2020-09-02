from django.urls import path
from .views import PostsListView
from . import views

urlpatterns = [
    path('', PostsListView.as_view(), name="blog-home"),
    path('about/', views.about_view, name="blog-about"),
]
