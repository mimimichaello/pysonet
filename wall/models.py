from django.db import models
from django.conf import settings
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

from comments.models import AbstractComment


class Post(models.Model):
    """ Post model
    """

    text = models.TextField(max_length=1024)
    create_data = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    moderation = models.BooleanField(default=True)
    view_count = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Post by {self.user}"

    def comments_count(self):
        return self.comments.count()


class Comment(AbstractComment, MPTTModel):
    """Comment model for Post"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    parent = TreeForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.user} - {self.post}"
