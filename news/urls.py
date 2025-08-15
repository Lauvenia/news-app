from django.urls import path
from .views import (
    home,
    create_article,
    article_detail,
    article_update,
    delete_article,
    create_newsletter,
    newsletter_detail,
    newsletter_update,
    delete_newsletter,
    list_articles_and_newsletters,
    approve,
    subscribe_to_journalist,
    subscribe_to_publisher,
)

urlpatterns = [
    path("", home, name="home"),

    # Displays a list of all articles and newsletters for logged-in users
    path("dashboard/", list_articles_and_newsletters, name="dashboard"),

    # Page to create a new article (restricted to journalists)
    path("article/new/", create_article, name="create_article"),

    # Displays the details of a single article based on its ID (pk
    path("article/<int:pk>/", article_detail, name="article_detail"),

    # Page to edit an existing article (restricted to author or editor)
    path("article/<int:pk>/edit/", article_update, name="article_update"),

    # Deletes a specific article by ID (restricted to author or editor)
    path("article/<int:pk>/delete/", delete_article, name="delete_article"),

    # Allows an editor to approve an article, triggering email/tweet notifications
    path("article/<int:pk>/approve/", approve, name="approve"),
    
    path("newsletter/new/", create_newsletter, name="create_newsletter"),
    path("newsletter/<int:pk>/", newsletter_detail, name="newsletter_detail"),
    path("newsletter/<int:pk>/edit/", newsletter_update, name="newsletter_update"),
    path("newsletter/<int:pk>/delete/", delete_newsletter, name="delete_newsletter"),
    path(
        "article/journalist-subscribe/<int:pk>/",
        subscribe_to_journalist,
        name="subscribe_to_journalist",
    ),
    path(
        "article/publisher-subscribe/<int:pk>/",
        subscribe_to_publisher,
        name="subscribe_to_publisher",
    ),
]
