from django.shortcuts import render
from django.views import generic


class HomeView(generic.View):
    def get(self, *args, **kwarg):
        return render(self.request, 'index.html')


class test():
    pass
