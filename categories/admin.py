from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    list_display_links = ["name", "created_at"]
    search_fields = ["name"]
    list_filter = ["created_at"]

    class Meta:
        model = Category
