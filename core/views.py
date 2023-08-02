from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from articles.models import Article


@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles": articles
    }

    return render(request, "dashboard.html", context)


def about(request):
    return render(request, "about.html")
