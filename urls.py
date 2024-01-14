from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',                  views.index),
    url(r'^post/(?P<id>.+)/$',  views.post),
    url(r'^tag/(?P<tag>.+)/$',  views.by_tag),
]
