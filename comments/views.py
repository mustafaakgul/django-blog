from django.shortcuts import render


def addComment(request, id):
    article = get_object_or_404(Article, id = id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")   #formdaki name e gore aliyor
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author = comment_author, comment_content = comment_content)
        newComment.article = article
        newComment.save()
        msg = "Tebrikler <strong> %s </strong> isimli gönderiniz başarıyla oluşturuldu." % (blog.title)
        messages.success(request, msg, extra_tags='success')
    #return redirect("/articles/article" + str(id))
    return redirect(reverse("article:detail", kwargs={"id": id}))


@login_required(login_url=reverse_lazy('user-login'))
def add_or_remove_favorite(request, slug):
    data = {'count': 0, 'status': 'deleted'}
    blog = get_object_or_404(Blog, slug=slug)
    favori_blog = FavoriteBlog.objects.filter(blog=blog, user=request.user)
    if favori_blog.exists():
        favori_blog.delete()
    else:
        FavoriteBlog.objects.create(blog=blog, user=request.user)
        data.update({'status': 'added'})
    count = blog.get_favorite_count()
    data.update({'count': count})

    return JsonResponse(data=data)


@login_required(login_url=reverse_lazy('user-login'))
def post_list_favorite_user(request, slug):
    page = request.GET.get('page', 1)
    blog = get_object_or_404(Blog, slug=slug)
    user_list = blog.get_added_favorite_user_as_object()
    paginator = Paginator(user_list, 1)
    try:
        user_list = paginator.page(page)
    except PageNotAnInteger:
        user_list = paginator.page(1)
    except EmptyPage:
        user_list = paginator.page(paginator.num_pages)
    my_fallowed_user = Fallowing.get_fallowed_username(request.user)
    html = render_to_string('blog/include/favorite/favorite-user-list.html',
                            context={'my_fallowed_user': my_fallowed_user, 'user_list': user_list},
                            request=request)

    page_html = render_to_string('blog/include/favorite/buttons/show_more_button.html',
                                 context={'post': blog, 'user_list': user_list}, request=request)

    return JsonResponse(data={'html': html, 'page_html': page_html})


def addComment(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author=comment_author, comment_content=comment_content)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail", kwargs={"id": id}))
