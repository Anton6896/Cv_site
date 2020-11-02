from django.shortcuts import render
from django.views import generic


class HomeView(generic.View):
    def get(self, *args, **kwarg):
        return render(self.request, 'index.html')


class UpdateProfileView(generic.UpdateView):
    pass


class MyRegisterView(generic.View):
    def get(self, *args, **kwarg):
        return render(self.request, 'register.html')

    def post(self, *args, **kwarg):
        pass