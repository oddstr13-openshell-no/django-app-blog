from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',                  views.index),
    url(r'^post/(?P<id>.+)/$',  views.post, name='blog-post'),
    url(r'^tag/(?P<tag>.+)/$',  views.by_tag, name='blog-by-tag'),
]
