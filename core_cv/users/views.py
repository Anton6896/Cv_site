from django.shortcuts import render, redirect
from django.views import generic
from . import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class HomeView(generic.View):
    def get(self, *args, **kwarg):
        return render(self.request, 'index.html')


class MyRegisterView(generic.CreateView):
    form_class = forms.UserRegisterForm_my
    template_name = "register.html"
    success_url = reverse_lazy("users:login")


# todo user profile update / change form
class UpdateProfileView(generic.UpdateView):
    pass
