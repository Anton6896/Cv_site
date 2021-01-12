from django.shortcuts import render
from django.views.generic import View,


class BlogListView(View):
    def get(self, *args, **kwarg):

        context = {
            'title': 'Blog',
        }
        return render(self.request, 'blog_list.html')
