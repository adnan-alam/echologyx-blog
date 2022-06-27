from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View, TemplateView


class HomeView(LoginRequiredMixin, TemplateView, View):
    template_name = "blog/home.html"
