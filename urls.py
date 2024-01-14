from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$',                  views.index),
    re_path(r'^post/(?P<id>.+)/$',  views.post, name='blog-post'),
    re_path(r'^tag/(?P<tag>.+)/$',  views.by_tag, name='blog-by-tag'),
]
