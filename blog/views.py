from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from .models import Post, Comment


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    queryset = Post.objects.all().order_by("-created_at")
    template_name = "blog/home.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
