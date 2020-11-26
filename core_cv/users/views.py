from django.shortcuts import render
from django.views import generic


class HomeView(generic.View):
    def get(self, *args, **kwarg):
        return render(self.request, 'index.html')


# todo user profile creation after resister
class UpdateProfileView(generic.UpdateView):
    pass


# todo user register form
class MyRegisterView(generic.View):
    def get(self, *args, **kwarg):
        return render(self.request, 'register.html')

    def post(self, *args, **kwarg):
        pass


class LogInView_My(generic.View):

    def get(self, *args, **kwarg):
        return render(self.request, 'login.html')
