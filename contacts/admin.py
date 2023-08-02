from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.fields]
    list_display_links = ["email", "phone", "created_at"]
    search_fields = ["email", "phone"]
    list_filter = ["email", "created_at"]

    class Meta:
        model = Contact
