from django.contrib import admin
from .models import ProjectCategory, Bid, ProjectSeries, Project
from tinymce.widgets import TinyMCE
from django.db import models


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ["title", "date"]}),
        ("Category", {"fields": ["project_category"]}),
        ("Series", {"fields": ["project_series"]}),
        ("URL", {"fields": ["project_slug"]}),
        ("Expiry", {"fields": ["expires"]}),
        ("Credentials", {"fields": ["credentials"]}),
        ("Description", {"fields": ["description"]}),
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }


# project proposal credential bid date
class BidAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Project", {"fields": ["title", "project"]}),
        ("Proposal", {"fields": ["proposal"]}),
        ("Credential", {"fields": ["credential"]}),
        ("Bid Date", {"fields": ["bid_date"]}),
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }


admin.site.register(ProjectCategory)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectSeries)
admin.site.register(Bid, BidAdmin)

# Register your models here.
