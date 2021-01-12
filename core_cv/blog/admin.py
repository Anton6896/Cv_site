from django.contrib import admin
from . import models


class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['pk', "title", "created_at"]
    list_display_links = ['pk', "title" ]


admin.site.register(models.Blog, BlogModelAdmin)
