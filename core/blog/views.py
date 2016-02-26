from django.shortcuts import render
from .models import Blog
from django.conf import settings
from django.views.generic import View
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.

def getBlogList(page=None):
    Blogs = Blog.objects.filter(status='p', isShown=True).order_by("-createTime")[settings.SINGLE_PAGE_LIMIT*page: settings.SINGLE_PAGE_LIMIT*(page+1)]
    length = len(list(Blog.objects.filter(status='p', isShown=True)))
    return Blogs, length

def getArticle(article=None):
    if article == -1: return
    article = Blog.objects.filter(status='p', isShown=True, id=article)[0]
    return article


@xframe_options_exempt
class BlogIndex(View):
    def get(self, request, page=None):
        page = 0 if page == None else int(page)
        data, length = getBlogList(page)
        flag = 1 if length>settings.SINGLE_PAGE_LIMIT*(page+1) else 0
        return render(request, 'Home/index.html', {"blogs": data, "next_page": page+1, "pre_page": page-1, "isNext": flag})


@xframe_options_exempt
class BlogDetail(View):
    def get(self, request, article=None):
        article = -1 if article == None else int(article)
        article = getArticle(article)
        return render(request, 'BlogDetail/BlogBase.html', {"article": article})
