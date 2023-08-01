from django.contrib import admin
from .models import Article, Comment

admin.site.register(Comment)
# admin.site.register(Article) OR with decorator
# admin panelini ozellstrecegmz class olstrcaz
#article ile ArticleAdmin baglamak icin meta yazdk ici ice class ile ismi meta olmali django ypms
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    #hangisleri gozuksun
    list_display = ["title", "author", "created_date"]
    #hangilerine tıklanrsa gidilsin
    list_display_links = ["title", "created_date"]
    #title bilgiseine gore arama yapmak
    search_fields = ["title"]
    #tarihe gore filtreleme
    list_filter = ["created_date"]
    class Meta:
        model = Article



"""
from django.contrib import admin

# Register your models here. .model bu kasrdeki
from .models import Article,Comment
#admin.site.register(Article)
#ozellestirilen admin panelndeki article

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    #meta gelen default class
    list_display = ["title", "author", "created_date"]
    list_display_links = ["title", "author"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    class Meta:
        model = Article


from django.contrib import admin
#.models bu kalsrdeki models git
from .models import Article

# Register your models here.

# admin.site.register(Article) OR with decorator
# admin panelini ozellstrecegmz class olstrcaz
#article ile ArticleAdmin baglamak icin meta yazdk ici ice class ile ismi meta olmali django ypms
class ArticleAdmin(admin.ModelAdmin):
    #hangisleri gozuksun
    list_display = ["title", "author", "created_date"]
    #hangilerine tıklanrsa gidilsin
    list_display_links = ["title", "created_date"]
    #title bilgiseine gore arama yapmak
    search_fields = ["title"]
    #tarihe gore filtreleme
    list_filter = ["created_date"]
    class Meta:
        model = Article


        # admin.site.register(Article) OR with decorator
# admin panelini ozellstrecegmz class olstrcaz
#article ile ArticleAdmin baglamak icin meta yazdk ici ice class ile ismi meta olmali django ypms
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    #hangisleri gozuksun
    list_display = ["title", "author", "created_date"]
    #hangilerine tıklanrsa gidilsin
    list_display_links = ["title", "created_date"]
    #title bilgiseine gore arama yapmak
    search_fields = ["title"]
    #tarihe gore filtreleme
    list_filter = ["created_date"]
    class Meta:
        model = Article
"""