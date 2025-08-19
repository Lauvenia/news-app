from django.db import models
from django.contrib.auth import get_user_model


class Publisher(models.Model):
    """
    MOdel to create a Publisher role
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    Model to create an article
    fields: title, content, is_approved, author, publisher, created_at
    """

    title = models.CharField(max_length=255)
    content = models.TextField(max_length=400, default="", blank=False)
    is_approved = models.BooleanField(default=False)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="articles"
    )
    publisher = models.ForeignKey(
        "Publisher",
        on_delete=models.CASCADE,
        related_name="articles",
        null=True,
        blank=True,
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Newsletter(models.Model):
    """
    Model to create a newsletter
    fields: title, content, created_at, author
    """
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=400, default="", blank=False)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="newsletters"
    )

    def __str__(self):
        return self.title
