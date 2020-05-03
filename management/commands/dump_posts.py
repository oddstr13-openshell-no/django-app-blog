#!/usr/bin/env python
import os
import json

from django.core.management.base import BaseCommand, CommandError

from blog.models import Post

"""
class Post(models.Model):
    title       = models.CharField(max_length=256)
    text        = models.TextField()
    user        = models.ForeignKey(User, on_delete=models.PROTECT, related_name="posts")
    published   = models.DateTimeField(blank=True, null=True) # Check this before showing
    tags        = TaggableManager(blank=True)
    frontpage   = models.BooleanField(default=False)
"""

OUTPUT = os.path.join('dump', 'blog')

class Command(BaseCommand):
    help = 'Dumps blog entries'

    def handle(self, *args, **options):
        if not os.path.exists(OUTPUT):
            os.makedirs(OUTPUT)
        
        for p in Post.objects.all():
            with open(os.path.join(OUTPUT, str(p.id)) + '.json', 'w') as fh:
                json.dump({
                    'id': p.id,
                    'title': p.title,
                    'content': p.text,
                    'author': p.user.username,
                    'published': p.published.isoformat(' '),
                    'tags': list(p.tags.names()),
                    'blog': p.frontpage,
                    
                }, fh)
