from django.db import models
from django.contrib.auth import get_user_model


class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
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
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=400, default="", blank=False)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="newsletters"
    )

    def __str__(self):
        return self.title
