from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class ProjectCategory(models.Model):
    project_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.project_category


# product Series
class ProjectSeries(models.Model):
    project_series = models.CharField(max_length=200)
    project_category = models.ForeignKey(ProjectCategory, default=1, verbose_name="Category", on_delete=models.PROTECT)
    series_summary = models.CharField(max_length=200)
    series_slug = models.CharField(max_length=200, default=1)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.project_series


class Project(models.Model):
    title = models.CharField(max_length=500, blank=False, null=False)
    date = models.DateTimeField("Project published on ", default=datetime.now())
    credentials = models.TextField()
    description = models.TextField()
    project_series = models.ForeignKey(ProjectSeries, default=1, verbose_name="Series", on_delete=models.PROTECT)
    project_category = models.ForeignKey(ProjectCategory, default=1, verbose_name="Series", on_delete=models.PROTECT)
    owner = models.ForeignKey(User, default=1, related_name="events", null=False, on_delete=models.PROTECT)
    expires = models.DateTimeField("Project expiries on", default=datetime.now())
    project_slug = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Project"

    def __str__(self):
        return self.title


class Bid(models.Model):
    project = models.ForeignKey(Project, related_name="bids", on_delete=models.PROTECT)
    proposal = models.TextField()
    credential = models.FileField(blank=False, null=False, default=1)
    user = models.ForeignKey(User, related_name="bids", on_delete=models.PROTECT)
    bid_date = models.DateTimeField("Date of Bid", default=datetime.now())

    class Meta:
        verbose_name_plural = "Bids"

    def __str__(self):
        return self.user
