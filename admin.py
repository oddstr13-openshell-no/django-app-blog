from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "user", "frontpage")  # lens
    list_filter = ["frontpage", "published", "user", "tags"]
    search_fields = ["title", "tags", "user"]
    ordering = ["-published"]
    date_hierarchy = "published"


admin.site.register(Post, PostAdmin)
