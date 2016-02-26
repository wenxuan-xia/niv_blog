from django.contrib import admin
from .models import Blog, Tag
# Register your models here.
from django.db import models
from pagedown.widgets import AdminPagedownWidget

class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "abstract", "isShown", "createTime", "updateTime", "status"]
    list_per_page = 30
    search_fields = ["title", "status", "isShown"]
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }
    def get_form(self, request, obj=None, **kwargs):
        form = super(BlogAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['author'].initial = request.user
        return form



class TagsAdmin(admin.ModelAdmin):
    list_display = ["tag"]
    search_fields = ["tag"]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagsAdmin)
