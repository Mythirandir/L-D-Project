from django.contrib import admin
from .models import Blog, Category
from tinymce.widgets import TinyMCE
from django.db import models


class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ["blog_title", "published"]}),
        ("Category", {"fields": ["blog_category"]}),
        ("URL", {"fields": ["blog_slug"]}),
        ("Blog Image", {"fields": ["blog_image"]}),
        ("Summary", {"fields": ["blog_summary"]}),
        ("Content", {"fields": ["blog_content"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
