from django.shortcuts import render
from django.views.generic import View
from django.views import generic
from . import models


class BlogListView(View):
    def get(self, *args, **kwarg):

        context = {
            'title': 'Blog',
        }

        return render(self.request, 'blog_list.html')


class ListOfBlogs(generic.ListView):
    model = models.Blog
    context_object_name = 'blogs_list'
    template_name = "blog_list.html"

    def get_queryset(self):
        return models.Blog.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListOfBlogs, self).get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context
