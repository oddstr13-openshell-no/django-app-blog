from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^$',                  'index'),
    url(r'^post/(?P<id>.+)/$',  'post'),
    url(r'^tag/(?P<tag>.+)/$',  'by_tag'),
)
