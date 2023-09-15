from django.shortcuts import render
from .models import kategori
from yazi.models import Yazi
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def index_view(request):
    kategoriler = kategori.objects.all()
    yazilar = Yazi.objects.all()

    paginator = Paginator(yazilar, 3)
    page = request.GET.get('sayfa')
    yazilar = paginator.get_page(page)

    return render(request, "kategoriler.html", {"kategoriler": kategoriler, "yazılar": yazilar})

def kategori_view(request, slug):
    kategoriler = kategori.objects.all()
    kategoriSecim = kategori.objects.get(slug=slug)

    yazilar = Yazi.objects.filter(kategori=kategoriSecim)

    paginator = Paginator(yazilar, 3)
    page = request.GET.get('sayfa')
    yazilar = paginator.get_page(page)

    return render(request, "kategoriler.html", {"kategoriler": kategoriler,
                                                "kategori": kategoriSecim, "yazılar": yazilar})