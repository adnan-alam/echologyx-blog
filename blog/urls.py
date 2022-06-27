from django.urls import path
from blog import views as views_blog


app_name = "blog"

urlpatterns = [
    path("", views_blog.HomeView.as_view(), name="home"),
]
