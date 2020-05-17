from django.db import models
from datetime import datetime


class Category(models.Model):
    blog_category = models.CharField(max_length=80)
    category_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.blog_category


class Blog(models.Model):
    blog_title = models.CharField(max_length=150)
    blog_image = models.ImageField()
    blog_category = models.ForeignKey(Category, default=1, verbose_name="Category", on_delete=models.PROTECT)
    blog_summary = models.CharField(max_length=250)
    published = models.DateTimeField("date published", default=datetime.now())
    blog_content = models.TextField()
    blog_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Blog"

    def __str__(self):
        return self.blog_title
