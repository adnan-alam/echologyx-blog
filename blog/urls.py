from django.urls import path
from blog import views as views_blog


app_name = "blog"

urlpatterns = [
    # blog urls
    path("", views_blog.PostListView.as_view(), name="home"),
    path("post/<slug:slug>", views_blog.PostDetailView.as_view(), name="post_detail"),
    path("post/create", views_blog.PostCreateView.as_view(), name="post_create"),
    path(
        "post/update/<slug:slug>",
        views_blog.PostUpdateView.as_view(),
        name="post_update",
    ),
    path(
        "post/delete/<slug:slug>",
        views_blog.PostDeleteView.as_view(),
        name="post_delete",
    ),
    # comment urls
    path(
        "comment/create", views_blog.CommentCreateView.as_view(), name="comment_create"
    ),
    path(
        "comment/update/<int:id>",
        views_blog.CommentUpdateView.as_view(),
        name="comment_update",
    ),
    path(
        "comment/delete/<int:id>",
        views_blog.CommentDeleteView.as_view(),
        name="comment_delete",
    ),
]
