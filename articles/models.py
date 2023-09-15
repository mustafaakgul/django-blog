from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
# from blog.abstract_models import DateAbstractModel
from django.contrib.auth.models import User


class Article(models.Model): # (DateAbstractModel):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="articles")
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

    def clean_icerik(self):
        icerik = self.cleaned_data.get('icerik')
        if len(icerik) < 250:
            uzunluk = len(icerik)
            msg = 'Lütfen en az 250 karakter giriniz. Girilen karakter sayısı (%s)' % (uzunluk)
            raise forms.ValidationError(msg)
        return icerik

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



#
# class Blog(models.Model):
#     YAYIN_TASLAK = ((None, 'Lütfen Birini Seçiniz'), ('yayin', 'YAYIN'), ('taslak', 'TASLAK'))
#     user = models.ForeignKey(User, default=1, null=True, verbose_name='User', related_name='blog')
#     title = models.CharField(max_length=100, blank=False, null=True, verbose_name='Başlık Giriniz',
#                              help_text='Başlık Bilgisi Burada Girilir.')
#     icerik = RichTextField(null=True, blank=False, max_length=5000, verbose_name='İçerik')
#     slug = models.SlugField(null=True, unique=True, editable=False)
#     image = models.ImageField(default='default/default-photo.jpg', upload_to=upload_to, blank=True,
#                               verbose_name='Resim',
#                               null=True,
#                               help_text='Kapak Fotoğrafı Yükleyiniz')
#     yayin_taslak = models.CharField(choices=YAYIN_TASLAK, max_length=6, null=True, blank=False)
#     unique_id = models.CharField(max_length=100, editable=True, null=True)
#     kategoriler = models.ManyToManyField(to=Kategori, blank=True, related_name='blog')
#     created_date = models.DateField(auto_now_add=True, auto_now=False)
#
#     class Meta:
#         verbose_name_plural = 'Gönderiler'
#         ordering = ['-id']
#
#     def __str__(self):
#         return "%s %s" % (self.title, self.user)
#
#     def get_added_favorite_user(self):
#         # self.favorite_blog.all() 1
#         return self.favorite_blog.values_list('user__username', flat=True)
#
#     def get_added_favorite_user_as_object(self):
#         data_list = []
#         qs = self.favorite_blog.all()
#         for obj in qs:
#             data_list.append(obj.user)
#         return data_list
#
#     def get_comment_count(self):
#         yorum_sayisi = self.comment.count()
#         if yorum_sayisi > 0:
#             return yorum_sayisi
#         return "Henüz Yorum Yok."
#
#     def get_favorite_count(self):
#         favori_sayisi = self.favorite_blog.count()
#         return favori_sayisi
#
#     @classmethod
#     def get_taslak_or_yayin(cls, taslak_yayin):
#         return cls.objects.filter(yayin_taslak=taslak_yayin)
#
#     def get_yayin_taslak_html(self):
#         if self.yayin_taslak == 'taslak':
#             return safe(
#                 '<span style="vertical-align:text-top;font-size:15px" class="label label-{1}">{0}</span>'.format(
#                     self.get_yayin_taslak_display(), 'danger'))
#         return safe('<span style="vertical-align:text-top;font-size:15px" class="label label-{1}">{0}</span>'.format(
#             self.get_yayin_taslak_display(), 'primary'))
#
#     def get_absolute_url(self):
#         return reverse('post-detail', kwargs={'slug': self.slug})
#
#     def get_image(self):
#         if self.image:
#             return self.image.url
#         else:
#             return '/media/default/default-photo.jpg'
#
#     def get_unique_slug(self):
#         sayi = 0
#         slug = slugify(unidecode(self.title))
#         new_slug = slug
#         while Blog.objects.filter(slug=new_slug).exists():
#             sayi += 1
#             new_slug = "%s-%s" % (slug, sayi)
#
#         slug = new_slug
#         return slug
#
#     def save(self, *args, **kwargs):
#         if self.id is None:
#             new_unique_id = str(uuid4())
#             self.unique_id = new_unique_id
#             self.slug = self.get_unique_slug()
#         else:
#             blog = Blog.objects.get(slug=self.slug)
#             if blog.title != self.title:
#                 self.slug = self.get_unique_slug()
#
#         super(Blog, self).save(*args, **kwargs)
#
#     def get_blog_comment(self):
#         # gönderiye ait tüm yorumları bana veren fonksiyon
#         return self.comment.all()
#
#     def get_blog_comment_count(self):
#         return len(self.get_blog_new_comment())
#
#     def get_blog_new_comment(self):
#         content_type = ContentType.objects.get_for_model(self)
#         object_id = self.id
#         all_comment = NewComment.objects.filter(content_type=content_type, object_id=object_id)
#         return all_comment
#
#
# class Comment(models.Model):
#     user = models.ForeignKey(User, null=True, default=1, related_name='comment')
#     blog = models.ForeignKey(Blog, null=True, related_name='comment')
#     # comment = models.ForeignKey(to='self', null=True)
#
#     icerik = models.TextField(verbose_name='Yorum', max_length=1000, blank=False, null=True)
#     comment_date = models.DateTimeField(auto_now_add=True, null=True)
#
#     class Meta:
#         verbose_name_plural = 'Yorumlar'
#
#     def __str__(self):
#         return "%s %s" % (self.user, self.blog)
#
#     def get_screen_name(self):
#         if self.user.first_name:
#             return "%s" % (self.user.get_full_name())
#         return self.user.username
#
#
# class NewComment(models.Model):
#     user = models.ForeignKey(User, null=True, default=1, related_name='+')
#     is_parent = models.BooleanField(default=False)
#
#     content_type = models.ForeignKey(to=ContentType, null=True)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')
#
#     icerik = models.TextField(verbose_name='Yorum', max_length=1000, blank=False, null=True)
#     comment_date = models.DateTimeField(auto_now_add=True, null=True)
#
#     def __str__(self):
#         username = self.user.username
#         text = "{0} {1}".format(username, self.content_type.model)
#         return text
#
#     class Meta:
#         verbose_name_plural = "İç içe yorum sistemi"
#
#     @classmethod
#     def add_comment(cls, nesne, model_type, user, icerik):
#         content_type = ContentType.objects.get_for_model(nesne.__class__)
#         cls.objects.create(user=user, icerik=icerik, content_type=content_type, object_id=nesne.pk)
#         if model_type == 'comment':
#             nesne.is_parent = True
#             nesne.save()
#
#     def get_child_comment(self):
#         if self.is_parent:
#             content_type = ContentType.objects.get_for_model(self.__class__)
#             all_child_comment = NewComment.objects.filter(content_type=content_type, object_id=self.pk)
#             return all_child_comment
#         return None
#
#
# class FavoriteBlog(models.Model):
#     user = models.ForeignKey(User, null=True, default=1, related_name='favorite_blog')
#     blog = models.ForeignKey(Blog, null=True, related_name='favorite_blog')
#
#     class Meta:
#         verbose_name_plural = 'Favorilere Eklenen Gönderiler'
#
#     def __str__(self):
#         return "%s %s" % (self.user, self.blog)
#
# @login_required
# def posts_list(request):
#     posts = Blog.objects.all()
#     page = request.GET.get('page', 1)
#     form = PostSorguForm(data=request.GET or None)
#     if form.is_valid():
#         taslak_yayin = form.cleaned_data.get('taslak_yayin', None)
#         search = form.cleaned_data.get('search', None)
#         if search:
#             posts = posts.filter(
#                 Q(icerik__icontains=search) | Q(title__icontains=search) | Q(
#                     kategoriler__isim__icontains=search)).distinct()
#         if taslak_yayin and taslak_yayin != 'all':
#             posts = posts.filter(yayin_taslak=taslak_yayin)
#             # posts =Blog.get_taslak_or_yayin(taslak_yayin)
#     paginator = Paginator(posts, 3)
#     try:
#         posts = paginator.page(page)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#
#     context = {'posts': posts, 'form': form}
#     return render(request, 'blog/post-list.html', context)
#
# @login_required(login_url=reverse_lazy('user-login'))
# def post_update(request, slug):
#     blog = get_object_or_404(Blog, slug=slug)
#     if request.user != blog.user:
#         return HttpResponseForbidden()
#     form = BlogForm(instance=blog, data=request.POST or None, files=request.FILES or None)
#     if form.is_valid():
#         form.save()
#         msg = "Tebrikler <strong> %s </strong> isimli gönderiniz başarıyla güncellendi." % (blog.title)
#         messages.success(request, msg, extra_tags='info')
#         return HttpResponseRedirect(blog.get_absolute_url())
#     context = {'form': form, 'blog': blog}
#     return render(request, 'blog/post-update.html', context=context)
#
# def post_delete(request, slug):
#     blog = get_object_or_404(Blog, slug=slug)
#     if request.user != blog.user:
#         return HttpResponseForbidden()
#     blog.delete()
#     msg = "<strong> %s </strong> isimli gönderiniz silindi." % (blog.title)
#     messages.success(request, msg, extra_tags='danger')
#     return HttpResponseRedirect(reverse('post-list'))
#
# @login_required(login_url=reverse_lazy('user-login'))
# def post_detail(request, slug):
#     form = CommentForm()
#     blog = get_object_or_404(Blog, slug=slug)
#     return render(request, 'blog/post-detail.html', context={'blog': blog, 'form': form})
#
#
# @login_required(login_url=reverse_lazy('user-login'))
# @is_post
# def add_comment(request, slug):
#     blog = get_object_or_404(Blog, slug=slug)
#     form = CommentForm(data=request.POST)
#     if form.is_valid():
#         new_comment = form.save(commit=False)
#         new_comment.blog = blog
#         new_comment.user = request.user
#         new_comment.save()
#         messages.success(request, 'Tebrikler Yorumunuz Başarıya Oluşturuldu.')
#         return HttpResponseRedirect((blog.get_absolute_url()))


class Yazi(models.Model):
    başlık = models.CharField(max_length=120)
    metin = RichTextField()
    yayinTarihi = models.DateTimeField(auto_now_add=True)
    image = models.FileField(null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)
    kategori = models.ForeignKey(kategori, on_delete=models.CASCADE, related_name="yazilar")
    begeniSayisi = models.IntegerField(default=0)
    goruntulenmeSayisi = models.IntegerField(default=0)

    def __str__(self):
        return self.başlık

    def get_unique_slug(self):
        slug = slugify(self.başlık)
        unique_slug = slug
        counter = 1

        while Yazi.objects.filter(slug=unique_slug).exists():
            unique_slug = slug + "-" + str(counter)
            counter += 1

        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()

        return super(Yazi, self).save(*args, **kwargs)