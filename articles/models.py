from django.db import models

from ckeditor.fields import RichTextField


class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Yazar ")
    title = models.CharField(max_length = 50,verbose_name = "Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(blank = True,null = True,verbose_name="Makaleye Fotoğraf Ekleyin")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "İsim")
    comment_content = models.CharField(max_length = 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']

# Create your models here. models class dan turet
class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Author")  #user foreigh key belirle slinrsede buda slnsn
    title = models.CharField(max_length=50)
    #content = models.TextField()
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True) #date vermicez o kullnsn demek ilk olustugnda
    #update_date = models.DateTimeField(auto_now=True) update edlnce tarih
    article_image = models.FileField(blank = True, null = True, verbose_name= "Image")
    #slug = models.SlugField(unique=True)  url lerde essiz yapilar olstrma burada detay daki gib id ler yerine ornegn title blgileri gsterleblr
    #https://www.youtube.com/watch?v=wH2Kl0sD-ao&list=PLPrHLaayVkhny4WRNp05C1qRl1Aq3Wswh&index=31
    def __str__(self):
        return self.title
    class Meta:  #siralamak icin en once eklenen ilk gsterlir tam tersiniide meta ile
        ordering = ["-created_date"]

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


"""
class Article(models.Model):
        #o user slinirse article larinida sil aautohot user olstrldu
        #author = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name = "Yazar")
        author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
        title = models.CharField(max_length = 50)
        #content = models.TextField()
        content = RichTextField()
        created_date = models.DateTimeField(auto_now_add = True)
        article_image = models.FileField(blank = True, null = True)

        #article lar  title ile grunsun demek
        def __str__(self):
                return self.title
"""

from django.db import models
from autoslug import AutoSlugField
#from blog.models import KategoriModel
from ckeditor.fields import RichTextField
# from blog.abstract_models import DateAbstractModel
from django.contrib.auth.models import User

"""
class YazilarModel(DateAbstractModel):
    resim = models.ImageField(upload_to='yazi_resimleri')
    baslik = models.CharField(max_length=50)
    icerik = RichTextField()
    slug = AutoSlugField(populate_from = 'baslik', unique=True)
    kategoriler = models.ManyToManyField(KategoriModel, related_name='yazi')
    yazar = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='yazilar')

    class Meta:
        verbose_name = 'Yazi'
        verbose_name_plural = 'Yazilar'
        db_table = 'Yazi'

    def __str__(self):
        return self.baslik
"""


class YazilarModel(models.Model):
    resim = models.ImageField(upload_to='yazi_resimleri', null=True, blank=True)
    baslik = models.CharField(max_length=50)
    icerik = models.TextField()
    content = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='baslik', unique=True)
    #kategoriler = models.ManyToManyField(KategoriModel, related_name='yazi')  # ters iliski kullanmak icin related yani
    # kategorideki butun yazilari grmek icin felan relatedlar burdan butun kategori modellere erisceksn ama kategori model
    # modelden butun yazılara olsmak icin
    yazar = models.ForeignKey(User, on_delete=models.CASCADE, related_name='yazilar')  # yazar üzerinden butun yazilara

    # eriseblmek icin related name kullanılır

    class Meta:
        verbose_name = 'Yazi'
        verbose_name_plural = 'Yazilar'
        db_table = 'Yazi'

    def __str__(self):
        return self.baslik



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