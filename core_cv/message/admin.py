from django.contrib import admin
from .models import Mesage, Comment


class MessageModelAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", ]
    list_display_links = ["title", "timestamp", ]
    list_filter = ["timestamp", ]
    search_fields = ["title", "content", ]
    list_editable = ["title"]

    class Meta:
        model = Mesage


admin.site.register(Mesage, MessageModelAdmin)
admin.site.register(Comment)
