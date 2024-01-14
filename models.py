from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager
import datetime



class Post(models.Model):
    title       = models.CharField(max_length=256)
    text        = models.TextField()
    user        = models.ForeignKey(User, on_delete=models.PROTECT, related_name="posts")
    published   = models.DateTimeField(blank=True, null=True) # Check this before showing
    tags        = TaggableManager(blank=True)
    frontpage   = models.BooleanField(default=False)
    
    def save(self):
        if not self.id:
            pass # Not created yet
        
        if self.published is None:
            self.published = datetime.datetime.now()
        
        super(Post, self).save()
    
    def __str__(self):
        return self.title
