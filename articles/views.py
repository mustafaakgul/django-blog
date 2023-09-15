from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse,Http404
from .forms import ArticleForm
from django.contrib import messages
from .models import Article
from comments.models import Comment
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


@login_required(login_url = "user:login")
def list_articles(request):
    """
    article_list = Article.objects.all()
    keyword = request.GET.get("keyword")
    if keyword:
        article_list = article_list.filter(title__icontains=keyword)
        #return render(request, "articles.html", {"articles": articles})
    paginator = Paginator(article_list, 5)
    page = request.GET.get("page")

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, "articles.html", {"articles": articles})
    """
    article_list = Article.objects.all()
    keyword = request.GET.get("keyword")
    if keyword:
        article_list = article_list.filter(
            Q(title__icontains=keyword)                |
            Q(content__icontains=keyword)              |
            Q(author__first_name__icontains=keyword)   |
            Q(author__last_name__icontains=keyword)
        ).distinct()
        # return render(request, "articles.html", {"articles": articles})
    paginator = Paginator(article_list, 5)
    page = request.GET.get("page")

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, "articles.html", {"articles": articles})


@login_required(login_url = "user:login")
def add_article(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    context = {
        "form" : form
    }

    if form.is_valid():
        article = form.save(commit=False) # When needed operations before saving
        article.author = request.user
        article.save()
        messages.success(request, "Article added successfully.")
        return redirect("core:dashboard")

    return render(request, "addarticle.html", context)


def get_article(request, id):
    #return HttpResponse("Detail : " + str(id))
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article, id = id)
    #return render(request, "detail.html", {"article": article})
    comments = article.comments.all()
    return render(request, "detail.html", {"article" : article, "comments" : comments})


@login_required(login_url = "user:login")
def update_article(request, id):
    if not request.user.is_authenticated():
        return Http404()

    article = get_object_or_404(Article, id=id) # get_object_or_404(Post, slug=slug)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    context = {
        'form': form
    }

    if form.is_valid():
        article = form.save(commit=False)  # Not saving yet because we get error if we don't assign user
        article.author = request.user
        article.save()
        messages.success(request, "Article updated successfully")
        return redirect("article:dashboard")

    return render(request, "article/update.html", context)


@login_required(login_url = "user:login")
def delete_article(request, id):
    if not request.user.is_authenticated(): # If not logged in
        return Http404()

    article = get_object_or_404(Article, id=id) # get_object_or_404(Post, slug=slug)
    article.delete()
    messages.success(request, "Article deleted sucessfully")
    return redirect("article:dashboard")

"""
def index(request):
    #requeste karslk response don
    #return HttpResponse("Main")
    #requeste karsılk render etmek
    context = {
        "number1" : 10,
        "number2" : 20,
        "numbers" : [1,2,3,4,5,6]
    }
    return render(request, "index.html", context)

def addarticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():

        #hata verdiginden user da eklemek ic,in syle bir operasyn yapilir
        #form.save()
        #commit save save ben yaplcam sen ypma demek
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, "Article created")
        return redirect("index")

    return render(request, "addarticle.html", {"form" : form})

def detail(request, id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article, id=id)
    return render(request, "detail.html", {"article" : article})



    def index(request):
    #requeste karslk response don
    #return HttpResponse("Main")
    #requeste karsılk render etmek
    context = {
        "number1" : 10,
        "number2" : 20,
        "numbers" : [1,2,3,4,5,6]
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def detail(request, id):
    return HttpResponse("Detail: " + str(id))

def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles" : articles
    }
    return render(request, "dashboard.html", context)

def addarticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():

        #hata verdiginden user da eklemek ic,in syle bir operasyn yapilir
        #form.save()
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, "Article created")
        return redirect("index")

    return render(request, "addarticle.html", {"form" : form})

def detail(request, id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article, id=id)
    return render(request, "detail.html", {"article" : article})


"""

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .forms import ArticleForm
from .models import Article, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, "articles.html", {"articles": articles})
    articles = Article.objects.all()

    return render(request, "articles.html", {"articles": articles})


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user
        article.save()

        messages.success(request, "Makale başarıyla oluşturuldu")
        return redirect("article:dashboard")
    return render(request, "addarticle.html", {"form": form})


def detail(request, id):
    # article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article, id=id)

    comments = article.comments.all()
    return render(request, "detail.html", {"article": article, "comments": comments})


@login_required(login_url="user:login")
def updateArticle(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user
        article.save()

        messages.success(request, "Makale başarıyla güncellendi")
        return redirect("article:dashboard")

    return render(request, "update.html", {"form": form})


def addComment(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author=comment_author, comment_content=comment_content)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail", kwargs={"id": id}))


from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def post_index(request):
    post_list = Post.objects.all()

    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()

    paginator = Paginator(post_list, 5)  # Show 5 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, "post/index.html", {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'post': post,
        'form': form
    }
    return render(request, "post/detail.html", context)


def post_create(request):
    # if request.method == "POST":
    #     print(request.POST)
    #
    # title = request.POST.get("title")
    # content = request.POST.get("metin")
    # Post.objects.create(title=title, content=content)

    # if request.method == "POST":
    #     # Formdan gelen bilgileri kaydet
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     # Formu kullanıcıya göster
    #     form = PostForm()

    if not request.user.is_authenticated():
        # Eğer kullanıcı giriş yapmamış ise hata sayfası gönder
        return Http404()

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, "Başarılı bir şekilde oluşturdunuz.", extra_tags='mesaj-basarili')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, "post/form.html", context)



from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Yazi, Yorum
from .forms import yaziEkleForm

# Create your views here.

def yazi_view(request, slug):
    yazimiz = Yazi.objects.get(slug=slug)
    yorumlar = Yorum.objects.filter(yazi=yazimiz)

    benzerYazilar = Yazi.objects.filter(kategori=yazimiz.kategori)[0:3]

    yazimiz.goruntulenmeSayisi += 1
    yazimiz.save()

    return render(request, "yazi/yaziDetay.html", {"yazi": yazimiz,
                                                   "yorumlar": yorumlar, "benzerYazilar": benzerYazilar})

def yaziEkle_view(request):
    form = yaziEkleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

        yazimiz = Yazi.objects.latest("id")

        return HttpResponseRedirect("/yazi/" + yazimiz.slug)

    return render(request, "yazi/yaziEkle.html", {"form": form})

def yorumEkle_view(request):
    metin = request.GET.get("yorumMetin")
    yaziId = request.GET.get("yaziId")

    if metin and yaziId:
        yazimiz = get_object_or_404(Yazi, id=yaziId)
        Yorum.objects.create(metin=metin, yazi=yazimiz)

        return HttpResponseRedirect("/yazi/" + yazimiz.slug)

def begen_view(request, id):
    yazimiz = Yazi.objects.get(id=id)
    yazimiz.begeniSayisi += 1
    yazimiz.save()

    return HttpResponseRedirect("/yazi/" + yazimiz.slug)