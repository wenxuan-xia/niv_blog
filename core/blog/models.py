from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    STATUS_CHOICES = (
        ('d', "draft"),
        ('p', "published"),
    )

    title = models.CharField("Title", max_length=128, db_index=True, )
    abstract = models.CharField("Abstract", max_length=128, default="")
    content = models.TextField("Content", )

    author = models.ForeignKey(User, verbose_name="author")
    tags = models.ManyToManyField("tag", blank=True)

    isShown = models.BooleanField("Visible", default=True)
    createTime = models.DateTimeField("Create Time", auto_now_add=True)
    updateTime = models.DateTimeField("Update Time", auto_now=True)
    status = models.CharField('Status', max_length=1, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])

    top = models.BooleanField("Set to Top", default=False)

class Tag(models.Model):
    tag = models.CharField("tag", max_length=50, db_index=True, )
    def __str__(self):
        return self.tag
