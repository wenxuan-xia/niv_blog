from django.conf.urls import patterns, url
from .views import BlogIndex, BlogDetail
from forms import FooModelForm



urlpatterns = [
    url(r'^$', BlogIndex.as_view()),
    url(r'^page_(?P<page>[0-9]+)/$', BlogIndex.as_view(), name="home"),
    url(r'^articles/(?P<article>[0-9]+)/$', BlogDetail.as_view()),
]
