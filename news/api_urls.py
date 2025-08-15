from django.urls import path
from .api_views import api_article_list

urlpatterns = [
    # Url patterns for rest-framework urls
    path("articles/", api_article_list, name="api_article_list"),
]