from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from django.utils import timezone

from blog.models import Post


def index(request):
    posts = (
        Post.objects.filter(frontpage=True)
        .filter(published__lte=timezone.now())
        .order_by("-published")
    )

    return render(request, "blog/index.html", {"posts": posts})


def by_tag(request, tag):
    posts = (
        Post.objects.filter(tags__name__in=[tag])
        .filter(published__lte=timezone.now())
        .order_by("-published")
    )

    return render(request, "blog/by_tag.html", {"posts": posts})


def post(request, id):
    _post = get_object_or_404(Post, id=id)

    return render(request, "blog/post.html", {"post": _post, "lpost": [_post]})
