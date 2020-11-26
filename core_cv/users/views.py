from django.shortcuts import render, redirect
from django.views import generic
from . import forms
from django.contrib import messages
from django.contrib.auth.models import User

class HomeView(generic.View):
    def get(self, *args, **kwarg):
        return render(self.request, 'index.html')


class LogInView_My(generic.View):

    def get(self, *args, **kwarg):
        return render(self.request, 'login.html')


# todo user register form
class MyRegisterView(generic.View):
    def get(self, *args, **kwarg):
        form = forms.UserRegisterForm_my()

        my_context = {
            "form" : form,
            "title" : "register",

        }

        return render(self.request, 'register.html', context=my_context)

    def post(self, *args, **kwarg):
        form = forms.UserRegisterForm_my(self.request.POST or None)

        if form.is_valid():
            form.save()

            u_name = form.cleaned_data.get('username')
            messages.success(self.request, f"nice to meet {u_name} !!")
            return redirect("users:home")
        else:
            form = forms.UserRegisterForm_my()



        
        
        
            








# todo user profile update / change form
class UpdateProfileView(generic.UpdateView):
    pass
