from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Post, Comment  # if Post already registered, keep it

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "created_at", "updated_at")
    list_filter = ("created_at", "author")
    search_fields = ("content", "author__username", "post__title")
