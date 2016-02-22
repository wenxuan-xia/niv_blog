from django.contrib import admin
from .models import Blog, Tag
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "abstract", "isShown", "createTime", "updateTime", "status"]
    list_per_page = 30
    search_fields = ["title", "status", "isShown"]

class TagsAdmin(admin.ModelAdmin):
    list_display = ["tag"]
    search_fields = ["tag"]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagsAdmin)
