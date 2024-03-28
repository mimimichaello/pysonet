from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from wall.models import Comment, Post


@admin.register(Post)
class CommentAdmin(admin.ModelAdmin):
    """ Посты"""

    list_display = ("user", "published", "create_data", "moderation", "view_count", "id")


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    """ Комментарии к постам"""
    list_display = ("user", "post", "created_data", "updated_data", "published", "id")
    # actions = ["unpublish", "publish"]
    mptt_level_indent = 15
