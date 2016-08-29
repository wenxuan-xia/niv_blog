from django.conf.urls import patterns, url
from .views import personalPage


urlpatterns = [
    url(r'^$', personalPage.as_view()),
]
