from django.contrib import admin
from .models import Article


# admin.site.register(Article) OR with decorator
# article ile ArticleAdmin baglamak icin meta yazdk ici ice class ile ismi meta olmali django ypms
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_at"]
    list_display_links = ["title", "created_at"]
    search_fields = ["title"]
    list_filter = ["created_at"]

    class Meta:
        model = Article
