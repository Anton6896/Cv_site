from django.shortcuts import render
from django.views.generic import View
from django.views import generic
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages


class ListOfPosts(generic.ListView):
    model = models.Blog
    context_object_name = 'blogs_list'
    template_name = "blog_list.html"
    paginate_by = 3

    def get_queryset(self):
        return models.Blog.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListOfPosts, self).get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context


class CreatePost(LoginRequiredMixin, generic.CreateView):
    model = models.Blog
    template_name = "create_blog_mess.html"
    fields = [
        'title',
        'content',
        'image',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user

        messages.success(
            self.request, f'Post created for {self.request.user.username}')

        return super().form_valid(form)


class DetailPost(generic.detail.DetailView):
    model = models.Blog
    template_name = "blog_detail.html"
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Blog Detail"
        return context
