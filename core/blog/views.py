from django.shortcuts import render
from django.http import Http404
from .models import Blog
from django.conf import settings

# Create your views here.

def getBlogList(page=None):
    Blogs = Blog.objects.filter(status='p', isShown=True)[settings.SINGLE_PAGE_LIMIT*page: settings.SINGLE_PAGE_LIMIT*(page+1)]
    length = Blog.objects.filter(status='p', isShown=True).count
    return Blogs, length


def BlogIndex(request, page=None):
    if page == None:
        page = 0
    page = int(page)
    data, length = getBlogList(page)
    flag = 1 if length>settings.SINGLE_PAGE_LIMIT*(page+1) else 1
    return render(request, 'Home/index.html', {"blogs": data, "next_page": page+1, "pre_page": page-1, "isNext": flag})

def BlogDetail(request, article=None):
    # data = getBlogList()
    return render(request, 'BlogDetail/BlogBase.html')
