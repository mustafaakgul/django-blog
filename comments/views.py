from django.shortcuts import render


def addComment(request, id):
    article = get_object_or_404(Article, id = id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")   #formdaki name e gore aliyor
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author = comment_author, comment_content = comment_content)
        newComment.article = article
        newComment.save()
    #return redirect("/articles/article" + str(id))
    return redirect(reverse("article:detail", kwargs={"id": id}))
