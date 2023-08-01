from django.db import models
from django.contrib.auth.models import User
from articles.models import YazilarModel
from blog.abstract_models import DateAbstractModel


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "İsim")
    comment_content = models.CharField(max_length = 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, verbose_name = "Article", related_name = "comments")
    #comment ile comment tabloasuna drek erisim related ile
    comment_author = models.CharField(max_length=50)
    comment_content = models.CharField(max_length=200)
    comment_date = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ["-comment_date"]


class Comment(models.Model):
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200, verbose_name='Ad Soyad')
    content = models.TextField(verbose_name='Yorum')

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class YorumModel(DateAbstractModel):
    yazan = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='yorum')
    yazi = models.ForeignKey(YazilarModel, on_delete=models.CASCADE, related_name='yorumlar')
    yorum = models.TextField()

    class Meta:
        db_table = 'yorum'
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'

    def __str__(self):
        return self.yazan.username




from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Post(models.Model):
    user = models.ForeignKey('auth.User', related_name='posts')
    title = models.CharField(max_length=120, verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")
    publishing_date = models.DateTimeField(verbose_name="Yayımlanma Tarihi", auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug': self.slug})
        # return "/post/{}".format(self.id)

    def get_create_url(self):
        return reverse('post:create', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post:update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post:delete', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-publishing_date', 'id']


class Comment(models.Model):
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200, verbose_name='Ad Soyad')
    content = models.TextField(verbose_name='Yorum')

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name