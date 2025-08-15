from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    roles = [("reader", "Reader"), ("journalist", "Journalist"), ("editor", "Editor")]
    role = models.CharField(max_length=15, choices=roles, blank=False)
    publisher = models.ForeignKey(
        "news.Publisher", on_delete=models.SET_NULL, null=True, blank=True
    )
    subscribed_journalists = models.ManyToManyField(
        "self",
        blank=True,
        limit_choices_to={"role": "journalist"},
        related_name="journalist_subscribers",
    )
    subscribed_publishers = models.ManyToManyField(
        "news.Publisher", blank=True, related_name="publisher_subscribers"
    )
