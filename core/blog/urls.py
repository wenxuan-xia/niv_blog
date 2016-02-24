from django.conf.urls import url
from django.contrib import admin
from django.views.defaults import page_not_found
from . import views

urlpatterns = [
    url(r'^$', views.BlogIndex),
    url(r'^page_(?P<page>[0-9]+)/$', views.BlogIndex),
    url(r'^articles/(?P<article>[0-9]+)/$', views.BlogDetail),
]
