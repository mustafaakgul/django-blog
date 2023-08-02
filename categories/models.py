from django.db import models
from autoslug import AutoSlugField


class Category(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    slug = AutoSlugField(populate_from='name', unique=True)   # Creates slug automatically
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
