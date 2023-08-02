from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.fields]
    list_display_links = ["content", "created_at"]
    search_fields = ["content"]
    list_filter = ["created_at"]

    class Meta:
        model = Comment
