from django.db import models


class AbstractComment(models.Model):
    """Abstract base class for comments"""

    text = models.TextField(max_length=512)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        abstract = True
