from django.db import models
from articles.models import Article
# from blog.abstract_models import DateAbstractModel


class Comment(models.Model): # (DateAbstractModel):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, related_name="comments")
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE, max_length = 50)
    content = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner

    class Meta:
        ordering = ['-created_at']
