from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
# from blog.abstract_models import DateAbstractModel
from django.contrib.auth.models import User


class Article(models.Model): # (DateAbstractModel):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Author")
    title = models.CharField(max_length=50, verbose_name="Title")
    # slug = AutoSlugField(populate_from='baslik', unique=True) SlugField(unique=True, editable=False, max_length=130)
    # slug = models.SlugField(unique=True)  url lerde essiz yapilar olstrma burada detay daki gib id ler yerine ornegn title blgileri gsterleblr
    content = RichTextField(max_length=2000) # models.TextField()
    image = models.FileField(blank=True, null=True, upload_to="articles/images/")
    #category = models.ManyToManyField(Category, verbose_name="Category", related_name="articles") # Inverse Relationship -> category.articles.all() related_name
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post:detail', kwargs={'slug': self.slug})
    #     # return "/post/{}".format(self.id)
    #
    # def get_create_url(self):
    #     return reverse('post:create', kwargs={'slug': self.slug})
    #
    # def get_update_url(self):
    #     return reverse('post:update', kwargs={'slug': self.slug})
    #
    # def get_delete_url(self):
    #     return reverse('post:delete', kwargs={'slug': self.slug})
    #
    # def get_unique_slug(self):
    #     slug = slugify(self.title.replace('ı', 'i'))
    #     unique_slug = slug
    #     counter = 1
    #     while Post.objects.filter(slug=unique_slug).exists():
    #         unique_slug = '{}-{}'.format(slug, counter)
    #         counter += 1
    #     return unique_slug
    #
    # def save(self, *args, **kwargs):
    #     self.slug = self.get_unique_slug()
    #     return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        # verbose_name = 'Article'
        # verbose_name_plural = 'Articles'
        # db_table = 'Article'
